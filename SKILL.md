---
name: jsfl-flash
description: Drive Adobe Flash/Animate through the flash-mcp bridge with JSFL. Use whenever the task involves the flash-mcp tools, JSFL scripting, .fla documents, the Flash timeline/stage/library, or drawing and animating in Flash/Animate. Covers the ES3 scripting dialect, the bridge's silent-failure mode, and the drawing/keyframe rules that make scripts work the first time.
---

# JSFL / Flash automation

Scripting Adobe Flash Professional through the `flash-mcp` bridge. The full API (855
documented methods and properties) is indexed in `api-index.md`, with per-object detail
files in `reference/`.

## Read this first: the silent-failure trap

**A `flash bridge not responding (timeout)` result almost never means Flash hung or that a
modal dialog is open. It means your JSFL threw a hard error.**

The bridge is a polling loop (`mcp/flash-mcp.jsfl`, run every second by a panel SWF). Per
command it: reads the inbox file, **deletes it**, `eval`s your code, then writes the result
to the outbox. Some Flash errors are *not* catchable JS exceptions — they abort the whole
script at the `eval`. When that happens the outbox write never runs, so the Python side
waits out its 120-second timeout and reports "not responding." The command is simply lost.

Consequences that matter:

- **Do not send keystrokes to the Flash window to "dismiss a dialog."** There is usually no
  dialog. It does nothing and wastes a minute.
- **The bridge is still alive.** The very next command works normally. Just fix the script.
- **A timeout costs 120 seconds.** Validate preconditions in-script instead of discovering
  errors by timing out.

### Getting the actual error message

`fl.trace()` output and Flash's error text go to the Output panel, which the bridge does not
return. Dump it to a file and read that:

```javascript
fl.outputPanel.save("file:///C:/path/to/scratch/out.txt", null, null)
```

The real error appears there as: `At line 120 of file "flash-mcp.jsfl": <message>`.
Line 120 is the bridge's `eval` — the message after it is what your code did wrong.

Not every failure aborts. Ordinary JavaScript errors (`x has no properties`, a bad property
name) *are* caught and come back as `{"ok": false, "error": "..."}` immediately — those are the
easy ones. The dangerous class is Flash's own operation errors, which tear down the script
regardless of any `try`/`catch` you wrap them in. Never trust `try`/`catch` to contain a risky
Flash call; check the precondition instead.

Because a timed-out command produces no trace output, prefer this pattern when probing:
write the command straight into the inbox folder yourself, then read the Output panel a few
seconds later. This never blocks for 120s:

```bash
# inbox: %APPDATA%/flash-mcp/inbox/<id>.json
{"id": "probe-1", "type": "run", "args": {"code": "...your jsfl..."}}
```

### Long scripts: bypass the MCP server

A script that runs more than a few seconds can kill the MCP stdio connection — the call comes
back `MCP error -32000: Connection closed` and the server restarts (you can tell because its
command-id counter resets to `1-…`). Flash itself is fine; the work is often *partially*
applied, which is worse than a clean failure.

The bridge is just files, so submit long work directly and skip the MCP layer entirely:
write `{"id": "...", "type": "run", "args": {"code": "<jsfl>"}}` into
`%APPDATA%/flash-mcp/inbox/<id>.json`, poll `outbox/<id>.result.json`, then dump the Output
panel. `runjsfl.py`, shipped next to this skill, does exactly that:

```bash
python runjsfl.py script.jsfl [timeout_seconds]
```

It prints the outbox result — or `NO RESULT (script aborted in Flash)` — followed by the
Output-panel tail, so traces and hard errors are both visible. Use it for anything looping
over many frames or layers; it never blocks the session.

## The scripting dialect is ES3

The JSFL engine is old JavaScript. These are **not available**:

- `JSON.parse` / `JSON.stringify` — build strings by hand (`"a=" + x`)
- `Array.forEach` / `map` / `filter` / `indexOf`, `Object.keys`, `String.trim`
- `let` / `const`, arrow functions, template literals

Use `var`, C-style `for` loops, and string concatenation. Returning a value from your
snippet is fine; the bridge stringifies it.

## Drawing and keyframe rules

These four rules are the difference between a script that works and one that times out.
Each was established by debugging a real failure.

### 1. Set `currentFrame` before drawing

Drawing goes into the *current frame of the current layer*. If the playhead sits on a frame
where the target layer has no frame, the script dies with:

> There is no current frame to draw into. Also check that the current frame is not an
> interpolated frame.

This bites when building several layers in a loop: inserting keyframes leaves the playhead
at frame 3, so the next layer's draw fails. Always reset:

```javascript
tl.currentFrame = 0;
tl.setSelectedLayers(idx, true);
tl.currentLayer = idx;
```

Also note `insertKeyframe(f)` duplicates frame `f-1`, so position the playhead at `f-1`
first, then insert, then move to `f`.

### 2. Never use `document.selectAll()` on a multi-layer figure

`selectAll()` grabs every element on **every unlocked layer** at the current frame. Rotating
"the arm" then rotates the legs, body, and head too — silently, with no error. Symptoms are
limbs that drift to nonsense coordinates.

Select only the elements you own:

```javascript
function selOwn(li, fi){
  var f = tl.layers[li].frames[fi];
  var sel = [];
  for (var i = 0; i < f.elements.length; i++) sel.push(f.elements[i]);
  doc.selection = sel;
  return sel.length;
}
```

This same helper is how you reliably apply a fill: `setFillColor` acts on the selection, and
a freshly drawn shape is not always left selected the way you expect.

### 3. Rotation needs an explicit transformation point

`rotateSelection(angle, true)` turns around the transformation point, which resets per
selection. Set it every time, and rotate by the **delta** from the previous frame's angle,
since rotation is relative:

```javascript
selOwn(idx, f);
doc.setTransformationPoint({x: pivotX, y: pivotY});
doc.rotateSelection(targetAngle - prevAngle, true);
prevAngle = targetAngle;
```

### 4. Clean slate idiom

Deleting layers is not enough (see below). To reset a document to one empty layer, one empty
frame, and an empty library:

```javascript
while (tl.layerCount > 1) tl.deleteLayer(tl.layerCount - 1);
tl.setSelectedLayers(0, true); tl.currentLayer = 0; tl.currentFrame = 0;
var fc = tl.layers[0].frameCount;
if (fc > 1) tl.removeFrames(1, fc);
tl.clearKeyframes(0, 1);
doc.selectNone();
var lib = doc.library;
lib.selectAll();
if (lib.getSelectedItems().length) lib.deleteItem();
```

### 5. Stale frames survive layer cleanup

Deleting layers and clearing frame 0 does **not** clear frames 1..n of a surviving layer.
Rebuilding on a dirty document leaves ghost art in later frames that is invisible at frame 0.

When a build goes wrong, start from a genuinely fresh document rather than clearing in place.
`fl.saveDocument` fails if a document with that filename is already open — close the old one
first:

```javascript
var docs = fl.documents;
for (var i = 0; i < docs.length; i++){
  if (docs[i].name == "thing.fla"){ fl.closeDocument(docs[i], false); break; }
}
fl.saveDocument(fl.getDocumentDOM(), "file:///C:/.../thing.fla");
```

## The #1 cause of aborts: an empty selection

Selection-dependent methods **abort the entire script** when nothing is selected. The docs
say this outright for `document.crop()` ("If no objects are selected, calling this method
results in an error and the script breaks at that point"), and it holds for the whole family:
`convertToSymbol`, `rotateSelection`, `setFillColor`, `deleteSelection`, `group`, `align`,
and friends.

Verified: `doc.selectNone(); doc.convertToSymbol('graphic','x','top left');` prints the trace
before it, then dies at the `eval` — no result, 120-second timeout.

So **guard every selection-dependent call**:

```javascript
if (doc.selection.length === 0){ fl.trace("nothing selected — skipping"); }
else { doc.convertToSymbol("graphic", "name", "top left"); }
```

Selection *does* survive between separate bridge commands (verified), but rebuilding it in
the same command that uses it is safer and costs nothing.

Note the contrast — these two fail very differently:

- **Empty selection** → hard abort, no result, 120s timeout.
- **Duplicate symbol name** → *silent no-op*. `convertToSymbol` returns null, the library is
  unchanged, the script keeps running and reports success. Check `library.items.length`
  before and after if it matters.

## Calls that need care

- **`convertToSymbol` works fine** — it is not broken in this build. Valid `registrationPoint`
  values include `"top left"`, `"top center"`, `"center"`, etc.; type is `"movie clip"`,
  `"button"`, or `"graphic"`. It turns the stage shape into an `instance` element whose
  `libraryItem` points at the new symbol. For simple rigs you don't need it — `rotateSelection`
  works directly on raw shapes.
- **Locked or hidden layers** — drawing onto one fails. If a script dies partway it may leave
  layers locked; unlock everything at the start of the next attempt.
- **Exporting to a folder that doesn't exist** — hard abort. Create it first:
  `if (!FLfile.exists(dir)) FLfile.createFolder(dir);`
- **`exportPNG(uri, bCurrentSettings, bCurrentFrame)`** — pass `true` for `bCurrentSettings`,
  or Flash opens the Export dialog and really does block. Exported PNGs keep alpha, so
  composite them onto a background before viewing or "transparent" reads as black.
- **`library.findItemIndex(name)` returns `null`, not `-1`, for a missing item.** `null < 0` is
  false *and* `null >= 0` is true, so both of the obvious guards are wrong. Scan
  `library.items` by name instead.
- **`library.addItemToDocument()` intermittently does nothing** while still reporting success.
  Check that the frame's element count actually grew and retry a few times.
- **`timeline.insertFrames(n)`** inserts *n* frames at the playhead — it is additive, not
  "extend the layer to frame n".
- **`timeline.addNewLayer(name, type, bAddAbove)`** inserts relative to the current layer, so
  **existing layer indices shift**. Re-resolve indices by name after adding layers.
- **`document.save()` vs `fl.saveDocument(doc, uri)`** — the former needs a prior save; the
  latter takes a `file:///` URI and is what the bridge's `save_file` uses. `saveDocument`
  fails if another open document already uses that filename.

## Animation: symbols and tweens

### Convert the artwork to a symbol *before* tweening

`timeline.createMotionTween()` will "convert each frame's contents to a single symbol
instance if necessary" — and its idea of *necessary* is per keyframe. Run it over raw shapes
spanning three keyframes and you get a library full of auto-named `Tween 1`, `Tween 2`, with
one keyframe sometimes left as a **raw shape**. A classic tween cannot interpolate from an
instance to a raw shape, so that span silently doesn't animate: the object holds its pose,
then snaps at the next keyframe. Nothing errors.

Do this instead — convert once, then let `insertKeyframe` duplicate that instance:

```javascript
doc.selection = /* the drawn shape */;
doc.convertToSymbol("graphic", "ballArt", "center");   // once, before any keyframes
tl.currentFrame = 0;  tl.insertKeyframe(12);           // duplicates the same instance
tl.currentFrame = 12; /* move it */
tl.createMotionTween(0, 24);
```

Verify afterwards that every keyframe points at the same symbol — this check catches the
failure immediately:

```javascript
for (var f = 0; f < L.frameCount; f++){
  var fr = L.frames[f];
  if (fr.startFrame !== f) continue;         // keyframes only
  var e = fr.elements[0];
  // e.libraryItem.name should be identical across all keyframes,
  // and e.elementType should be "instance", never "shape"
}
```

A clean build leaves the library with only your own symbols — stray `Tween N` entries are the
tell that something was auto-converted.

### Graphic vs movie clip: only graphics animate on the Stage

A **movie clip**'s internal timeline does **not** advance on the authoring Stage or in
`exportPNG` — it only runs in the published SWF. Export a nested movie-clip animation frame by
frame and the inner motion is frozen at frame 0 while the outer tween moves normally.

**Graphic** symbols sync their internal timeline to the parent, so they render correctly in
stage exports. For anything you intend to inspect via PNG export, use `"graphic"` and set the
instance's playback mode:

```javascript
e.symbolType = "graphic";
e.loop = "loop";        // or "play once" / "single frame"
e.firstFrame = 0;       // graphic-only properties
```

`loop` and `firstFrame` are **undefined on movie-clip instances** — assigning them there is a
hard abort, and `try`/`catch` will not save you.

Critically, **an instance's `symbolType` is independent of its library item's**. Setting
`libraryItem.symbolType = "graphic"` does *not* retroactively convert instances already on the
Stage; you must set `symbolType` on each instance (including the one in every keyframe).

### Easing is per-tween, not per-axis

`frame.tweenEasing` runs −100..100: **positive = start fast, decelerate** (ease out);
**negative = start slow, accelerate** (ease in). Set it on the keyframe that *starts* the span.

It applies to the whole transform. Custom ease curves don't help either — `setCustomEase`
accepts only `"all"`, `"position"`, `"rotation"`, `"scale"`, `"color"`, `"filters"`, and
`"position"` means x and y together. **There is no way to ease x and y independently in one
tween.**

For projectile motion — constant horizontal speed, accelerating vertical — nest the motion:

1. A **graphic** symbol whose own timeline tweens only `y`, with `tweenEasing = 100` on the
   rise and `-100` on the fall.
2. On the parent timeline, tween that instance's `x` with `tweenEasing = 0`.

Verified result: `dx` constant every frame while `dy` runs −38 → −2 → +2 → +38, a clean
parabola.

### Shape tweens are the mirror image of motion tweens

Motion tweens need symbols; shape tweens need **raw shapes** and refuse to work on instances.
Build the destination on a *blank* keyframe so the two ends are genuinely different artwork:

```javascript
doc.addNewOval({...}, false, true);           // frame 0: raw shape
tl.currentFrame = 0; tl.insertBlankKeyframe(24);
tl.currentFrame = 24;
doc.addNewRectangle({...}, 0, false, true);   // frame 24: a different raw shape
doc.getTimeline().layers[0].frames[0].tweenType = "shape";   // direct assignment
```

Set it by **assigning `frame.tweenType` directly**. `timeline.setFrameProperty("tweenType",
"shape", 0, 1)` silently does nothing — that method only acts on *selected* frames, and it
fails quietly enough that the neighbouring `shapeTweenBlend` assignment still succeeds, which
makes it look like it worked.

Shape tweens interpolate **geometry and fill colour together** — a red circle morphing into a
blue square passes through purple rounded shapes, with no colour effect needed.
`frame.shapeTweenBlend` is `"distributive"` or `"angular"`. Shape hints are not in the JSFL
API at all.

### 3D: movie clips only, and the coordinate is an object

3D transforms apply through the document, not through element properties — there is no
`rotationX/Y/Z` in JSFL. The two calls are `document.rotate3DSelection(xyz, bGlobalTransform)`
and `document.translate3DSelection(xyz, bGlobalTransform)`, and both work **only on movie clip
instances**.

The coordinate must be an **object**, not an array:

```javascript
doc.setStageViewAngle(55);                            // perspective strength
doc.selection = [fr.elements[0]];                     // a movie clip instance
doc.rotate3DSelection({x:0, y:20, z:0}, false);       // NOT [0, 20, 0]
```

Passing an array fails with *"argument number 2 is invalid"* — a misleading message that
points at the wrong parameter.

Rotations are **relative and cumulative**, so animate by inserting a keyframe and applying the
same delta again on each one; `insertKeyframe` carries the accumulated 3D state forward.
`symbolInstance.is3D` flips to `true` once any 3D transform is applied, which is the cheapest
way to confirm it took. Verified: a card rotated +20° per keyframe narrows 160 → 131 → 91 → 40
→ 17 px (edge-on near 90°) and then widens again, with proper trapezoidal perspective.

### Inverse kinematics (Bone tool) is not scriptable

Searched the whole 631-page reference: **zero** occurrences of "armature", "bone", or "inverse
kinematics". The only trace of IK in the entire API is `layer.animationType`, which *reports*
`"none"`, `"motion object"`, or `"IK pose"`. Layer types are limited to `"normal"`, `"guide"`,
`"guided"`, `"mask"`, `"masked"`, `"folder"` — there is no armature layer type to create.

So armatures can only be built by hand in the authoring UI. A script can detect one
(`layer.animationType === "IK pose"`) and read its frames, but cannot create bones, pose them,
or convert a rig. For scripted character motion, rig it yourself with nested symbols and
rotation — as the walk-cycle and bouncing-ball recipes above do.

### Flash never depth-sorts, so build 3D yourself

`rotate3DSelection` / `translate3DSelection` really do apply 3D transforms, but Flash draws
sibling objects **in layer order, not by depth**. Assemble a cube from six 3D-placed faces and
the back faces paint over the front ones: the solid reads inside-out, and no amount of tweaking
angles fixes it. There is no z-sort to enable.

Two facts make this solvable:

1. **A convex solid needs no sorting once back faces are culled.** The at-most-three faces of a
   cube that point at the camera never overlap each other, so their draw order is irrelevant.
2. **Under orthographic projection every cube face is an exact parallelogram**, and a
   parallelogram is exactly what a 2D affine matrix produces. So skip Flash's 3D entirely and
   set `element.matrix` yourself.

Give each face an outward normal `n` and two in-plane axes `e1`, `e2` (keep `e1 × e2 = -n` on
all six so none comes out mirrored). For a rotation matrix `R`, with the cube centred at
`(cx, cy)` and half-edge `S`:

```
visible  ⟺  (R·n).z < 0            // z points into the screen
matrix   =  { a: (R·e1).x, b: (R·e1).y,
              c: (R·e2).x, d: (R·e2).y,
              tx: cx + (R·(S·n)).x, ty: cy + (R·(S·n)).y }
```

Place only the visible faces on one layer and assign each its matrix. The result is a solid,
correctly occluded cube at every orientation — verified across a full tumbling animation where
all 62 frames showed exactly three faces.

Two matching details matter:

- **`element.matrix` and Flash 3D are separate channels.** Once `is3D` is true the matrix reads
  back as the identity — a 3D orientation cannot be recovered (or set) through `matrix`. Use one
  or the other, never both on the same instance.
- **A camera tilt is just a rotation applied to everything.** Tilting the whole scene by
  `Rx(θ)` is the same as raising the camera by θ, and a flat horizontal band *is* the correct
  projection of a tabletop under it — so a scene drawn that way already agrees with the cube.

When an object comes to rest, snap its orientation carefully: it may only have turned about the
**world vertical** axis. Snapping the view-axis rotation to a multiple of 90° instead lets it
settle tipped about the axis pointing at the camera, which reads as inverted perspective — the
solid looks like it is being seen from underneath even though its silhouette is pixel-identical
to the correct one.

## Verifying work

Screenshots only show the current frame, so check the data as well as the picture:

```javascript
// element counts and positions across the animation
for (var f = 0; f < 4; f++){
  for (var l = 0; l < tl.layerCount; l++){
    var fr = tl.layers[l].frames[f];
    var e = fr.elements[0];
    // accumulate into a string, then fl.trace it once
  }
}
```

Then `fl.outputPanel.save(...)` and read the file. Two poses that should be mirror images
(e.g. a walk cycle's contact frames) are easy to confirm numerically and easy to miss by eye.

`take_screenshot` exports the current frame as PNG; combine with `select_frame` to inspect a
specific frame.

## Working checklist

1. `get_project_state` — know the document, layers, and frame counts.
2. Build in **small steps**, each verified. A 60-line script that dies gives you one useless
   timeout; six 10-line steps tell you exactly which call failed.
3. After each step, if it timed out: dump the Output panel and read the real error.
4. Verify geometry numerically, then visually.
5. Save with `doc.save()`.

## API reference

`api-index.md` lists every object and points to its file. The large ones:
`reference/document.md` (183 entries), `reference/fl.md` (79), `reference/timeline.md` (51),
`reference/frame.md` (41). Grep these rather than reading whole files:

```bash
grep -A4 'addNewRectangle' reference/document.md
```

Entries carry the exact `Usage` signature, parameter semantics, and return value from the
official *Extending Flash Professional* documentation.
