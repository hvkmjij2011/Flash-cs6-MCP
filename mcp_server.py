import ctypes
import json
import os
import re
import sys
import time
import uuid
from pathlib import Path

try:
    from fastmcp import FastMCP
except ImportError:
    print("fastmcp is required: pip install fastmcp", file=sys.stderr)
    raise

APP_DATA_DIR = Path(os.environ.get("APPDATA", str(Path.home() / "AppData" / "Roaming"))) / "flash-mcp"
INBOX = APP_DATA_DIR / "inbox"
OUTBOX = APP_DATA_DIR / "outbox"
LOGS = APP_DATA_DIR / "logs"
SCREENSHOTS = APP_DATA_DIR / "screenshots"

PACKAGE_DIR = Path(__file__).resolve().parent
CONFIG_FILE = PACKAGE_DIR / "config.json"
SCENES_DIR = PACKAGE_DIR.parent / "scenes"

mcp = FastMCP("flash-mcp")


def _as_uri_dir(path: Path) -> str:
    return Path(path).as_uri() + "/"


def _write_config() -> None:
    INBOX.mkdir(parents=True, exist_ok=True)
    OUTBOX.mkdir(parents=True, exist_ok=True)
    LOGS.mkdir(parents=True, exist_ok=True)
    SCREENSHOTS.mkdir(parents=True, exist_ok=True)
    config = {
        "inbox": _as_uri_dir(INBOX),
        "outbox": _as_uri_dir(OUTBOX),
        "log": (LOGS / "bridge.log").as_uri(),
        "screenshots": _as_uri_dir(SCREENSHOTS),
    }
    CONFIG_FILE.write_text(json.dumps(config, indent=2), encoding="utf-8")


def _clean_startup() -> None:
    stale_before = time.time() - 60
    for folder in (INBOX, OUTBOX):
        if folder.exists():
            for f in folder.iterdir():
                if f.is_file() and f.stat().st_mtime < stale_before:
                    f.unlink(missing_ok=True)


class Bridge:
    def __init__(self) -> None:
        self._seq = 0

    def submit(self, cmd_type: str, args: dict, timeout: float = 60.0) -> dict:
        self._seq += 1
        cid = str(self._seq) + "-" + uuid.uuid4().hex[:8]
        cmd = {"id": cid, "type": cmd_type, "args": args}
        inbox_file = INBOX / f"{cid}.json"
        out_file = OUTBOX / f"{cid}.result.json"
        inbox_file.write_text(json.dumps(cmd), encoding="utf-8")
        deadline = time.time() + timeout
        while time.time() < deadline:
            if out_file.exists():
                try:
                    result = json.loads(out_file.read_text(encoding="utf-8"))
                except json.JSONDecodeError:
                    time.sleep(0.2)
                    continue
                out_file.unlink(missing_ok=True)
                return result
            time.sleep(0.2)
        inbox_file.unlink(missing_ok=True)
        return {"ok": False, "error": "flash bridge not responding (timeout)"}


bridge = Bridge()


def normalize_doc_type(value: str) -> str:
    if value is None:
        return "timeline"
    s = str(value).strip().lower().replace(" ", "").replace("-", "").replace("_", "")
    if s in ("html5", "canvas", "html5canvas", "htmlcanvas"):
        return "htmlcanvas"
    return "timeline"


SCREENSIZES = {
    "fhd": (1920, 1080),
    "fullhd": (1920, 1080),
    "1080p": (1920, 1080),
    "hd": (1280, 720),
    "720p": (1280, 720),
    "qhd": (2560, 1440),
    "1440p": (2560, 1440),
    "2k": (2560, 1440),
    "4k": (3840, 2160),
    "uhd": (3840, 2160),
    "8k": (7680, 4320),
    "svga": (800, 600),
    "ntsc": (720, 480),
    "pal": (720, 576),
}


def parse_screensize(value: str) -> tuple:
    s = str(value).strip().lower().replace(" ", "")
    if s in SCREENSIZES:
        return SCREENSIZES[s]
    m = re.match(r"^(\d+)[x×](\d+)$", s)
    if m:
        return (int(m.group(1)), int(m.group(2)))
    m = re.match(r"^(\d+)[,;](\d+)$", s)
    if m:
        return (int(m.group(1)), int(m.group(2)))
    raise ValueError(f"cannot parse screensize: {value}")


NAMED_COLORS = {
    "red": "ff0000",
    "green": "00ff00",
    "blue": "0000ff",
    "black": "000000",
    "white": "ffffff",
    "yellow": "ffff00",
    "magenta": "ff00ff",
    "cyan": "00ffff",
    "orange": "ff8800",
}


def normalize_color(value, default="#000000") -> str:
    if value is None:
        return default
    s = str(value).strip().lower().lstrip("#")
    if s in NAMED_COLORS:
        s = NAMED_COLORS[s]
    if re.fullmatch(r"[0-9a-f]{6}", s):
        return "#" + s
    if re.fullmatch(r"[0-9a-f]{3}", s):
        return "#" + "".join(c * 2 for c in s)
    return default


def resolve_fla_uri(value: str) -> str:
    """Turns a file name or an absolute Windows path into a file:/// URI pointing to a .fla file.
    Bare names are placed in <flash>/scenes/."""
    s = str(value).strip()
    if re.match(r"^[A-Za-z]:[\\/]", s):
        p = Path(s)
    else:
        SCENES_DIR.mkdir(parents=True, exist_ok=True)
        p = SCENES_DIR / s
    if p.suffix.lower() != ".fla":
        p = p.with_suffix(".fla")
    return p.as_uri()


def line_jsfl(x1: int, y1: int, x2: int, y2: int, thickness: int, color: str) -> str:
    name = "%s_%d_%d,%d_%d,%d" % (color, thickness, x1, y1, x2, y2)
    return (
        "(function(){\n"
        "var doc = fl.getDocumentDOM();\n"
        "if (!doc) return 'error:no open document';\n"
        "var tl = doc.getTimeline();\n"
        "var name = 'line_" + name + "';\n"
        "var idx = tl.addNewLayer(name);\n"
        "if (typeof idx !== 'number') idx = tl.currentLayer;\n"
        "var x1=%d, y1=%d, x2=%d, y2=%d, th=%d;\n" % (x1, y1, x2, y2, thickness)
        + "var dx=x2-x1, dy=y2-y1;\n"
        "var len=Math.sqrt(dx*dx+dy*dy); if (len<0.01) len=1;\n"
        "var ang=Math.atan2(dy,dx)*180/Math.PI;\n"
        "var midX=(x1+x2)/2, midY=(y1+y2)/2;\n"
        "doc.addNewRectangle({left:0, top:-th/2, right:len, bottom:th/2}, 0);\n"
        "doc.selectNone();\n"
        "var els=tl.layers[idx].frames[0].elements;\n"
        "var sel=[];\n"
        "for(var i=0;i<els.length;i++) sel.push(els[i]);\n"
        "doc.selection=sel;\n"
        "doc.setFillColor('" + color + "');\n"
        "doc.selectNone();\n"
        "var el=tl.layers[idx].frames[0].elements[0];\n"
        "el.x=midX; el.y=midY; el.transformX=midX; el.transformY=midY; el.rotation=ang;\n"
        "return 'drew ' + name + ' on layer index ' + idx + ' (' + els.length + ' element(s))';\n"
        "})()"
    )


def rect_jsfl(x: int, y: int, width: int, height: int, color: str) -> str:
    x1, y1 = x, y
    x2, y2 = x + width, y
    x3, y3 = x + width, y + height
    x4, y4 = x, y + height
    name = "rect_%s_%d,%d_%d,%d_%d,%d_%d,%d" % (color, x1, y1, x2, y2, x3, y3, x4, y4)
    return (
        "(function(){\n"
        "var doc = fl.getDocumentDOM();\n"
        "if (!doc) return 'error:no open document';\n"
        "var tl = doc.getTimeline();\n"
        "var name = '" + name + "';\n"
        "var idx = tl.addNewLayer(name);\n"
        "if (typeof idx !== 'number') idx = tl.currentLayer;\n"
        "doc.addNewRectangle({left:%d, top:%d, right:%d, bottom:%d}, 0);\n" % (x1, y1, x3, y3)
        + "doc.selectNone();\n"
        "var els = tl.layers[idx].frames[0].elements;\n"
        "var sel = [];\n"
        "for (var i = 0; i < els.length; i++) sel.push(els[i]);\n"
        "doc.selection = sel;\n"
        "doc.setFillColor('" + color + "');\n"
        "doc.selectNone();\n"
        "return 'drew ' + name + ' on layer index ' + idx + ' (' + els.length + ' element(s))';\n"
        "})()"
    )


def draw_jsfl(draw_expr: str, color: str, layer_prefix: str) -> str:
    return (
        "(function(){\n"
        "var doc = fl.getDocumentDOM();\n"
        "if (!doc) return 'error:no open document';\n"
        "var tl = doc.getTimeline();\n"
        "var name = '" + layer_prefix + "_' + (tl.layerCount + 1);\n"
        "var idx = tl.addNewLayer(name);\n"
        "if (typeof idx !== 'number') idx = tl.currentLayer;\n"
        "doc." + draw_expr + ";\n"
        "doc.selectNone();\n"
        "var els = tl.layers[idx].frames[0].elements;\n"
        "var sel = [];\n"
        "for (var i = 0; i < els.length; i++) sel.push(els[i]);\n"
        "doc.selection = sel;\n"
        "doc.setFillColor('" + color + "');\n"
        "doc.selectNone();\n"
        "return 'drew ' + name + ' on layer index ' + idx + ' (' + els.length + ' element(s))';\n"
        "})()"
    )


@mcp.tool()
def get_project_state() -> str:
    """(beginner-tools) Returns the current state of the open project: name, size, frame rate,
    current frame and the list of layers with their frame counts."""
    result = bridge.submit("get_project_state", {}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def draw_rect(x: int, y: int, width: int, height: int, color: str = "#000000") -> str:
    """(beginner-tools) Draws a filled rectangle at (x, y) with the given width and height.
    Each shape gets its own new layer so colors stay isolated. Returns the created layer name.
    The layer is named `rect_#RRGGBB_x1,y1_x2,y2_x3,y3_x4,y4` (TL, TR, BR, BL corners) so
    one_point_move can move a single corner (making a trapezoid) later."""
    color = normalize_color(color)
    code = rect_jsfl(int(x), int(y), int(width), int(height), color)
    result = bridge.submit("run", {"code": code}, timeout=30.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def draw_oval(x: int, y: int, width: int, height: int, color: str = "#000000") -> str:
    """(beginner-tools) Draws a filled oval (ellipse) at (x, y) with the given width and height.
    Each shape gets its own new layer so colors stay isolated. Returns the created layer name."""
    color = normalize_color(color)
    bounds = "{left:%d, top:%d, right:%d, bottom:%d}" % (int(x), int(y), int(x) + int(width), int(y) + int(height))
    code = draw_jsfl("addNewOval(" + bounds + ", 0)", color, "shape")
    result = bridge.submit("run", {"code": code}, timeout=30.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def draw_line(x1: int, y1: int, x2: int, y2: int, color: str = "#000000", thickness: int = 3) -> str:
    """(beginner-tools) Draws a line from (x1, y1) to (x2, y2) on its own new layer.

    This Flash build has no addNewLine/drawingLayer, so the line is drawn as a thin rotated
    rectangle (color = fill color, thickness = line width). The layer is named
    `line_#RRGGBB_thickness_x1,y1_x2,y2` so one_point_move can move an endpoint later."""
    color = normalize_color(color)
    t = max(1, int(thickness))
    code = line_jsfl(int(x1), int(y1), int(x2), int(y2), t, color)
    result = bridge.submit("run", {"code": code}, timeout=30.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def move_shape(layer: int, x: int, y: int, frame: int | None = None) -> str:
    """(beginner-tools) Moves the shape on the given layer to a new position (x, y).

    x/y are the CENTER coordinates of the shape (Flash element.x/.y), 0-based stage units.
    The first element of that layer's frame is moved; `frame` defaults to the current frame."""
    args = {"layer": int(layer), "x": int(x), "y": int(y)}
    if frame is not None:
        args["frame"] = int(frame)
    result = bridge.submit("move_shape", args, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def one_point_move(layer: int, point: int, x: int, y: int, frame: int | None = None) -> str:
    """(beginner-tools) Moves one point of a shape drawn with draw_line or draw_rect.

    For a line: `point` selects which endpoint to move: 0 = the first endpoint (x1,y1 passed to
    draw_line), 1 = the second endpoint (x2,y2). The chosen endpoint moves to (x, y) and the line
    is redrawn between the moved point and the other, fixed endpoint, keeping its color and thickness.

    For a rectangle: `point` selects which corner to move: 0 = top-left, 1 = top-right,
    2 = bottom-right, 3 = bottom-left. The chosen corner moves to (x, y) and the rect becomes a
    trapezoid, keeping its fill color. This uses shape edge control points (setControl) since this
    Flash build cannot otherwise edit shape vertices."""
    args = {"layer": int(layer), "point": int(point), "x": int(x), "y": int(y)}
    if frame is not None:
        args["frame"] = int(frame)
    result = bridge.submit("one_point_move", args, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def new_project(type: str = "timeline", screensize: str = "FHD", fps: int = 24, name: str = "") -> str:
    """Creates a new Animate/Flash project.

    Accepts flexible type aliases (as3, actionscript3, actionscript 3.0, 3, standard,
    classical, html5, canvas, ...) and flexible screensize values (FHD, 1080p, 1920x1080, ...).
    If `name` is given (a file name like "intro" or an absolute path), the document is
    immediately saved under that name in <flash>/scenes (bare names) and gets that title.
    """
    try:
        width, height = parse_screensize(screensize)
    except ValueError as e:
        return json.dumps({"ok": False, "error": str(e)}, ensure_ascii=False)
    if fps is None or fps <= 0:
        fps = 24
    doc_type = normalize_doc_type(type)
    args = {
        "doc_type": doc_type,
        "width": width,
        "height": height,
        "fps": int(fps),
    }
    if name:
        args["name"] = resolve_fla_uri(name)
    result = bridge.submit("new_project", args)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def save_file(path: str = "") -> str:
    """(beginner-tools) Saves the open document.

    If `path` is given (a file name like "intro" -> <flash>/scenes/intro.fla, or an absolute
    path), the document is saved there without a dialog via fl.saveDocument and its title
    becomes that file name. If omitted, the document is re-saved under its current name
    (only works if it was saved at least once before)."""
    args = {}
    if path:
        args["path"] = resolve_fla_uri(path)
    result = bridge.submit("save_file", args, timeout=30.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def clear_scene() -> str:
    """(beginner-tools) Deletes every shape on the current frame across all layers."""
    result = bridge.submit("clear_scene", {}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def run_flash_command(jsfl_command: str) -> str:
    """Runs a raw JSFL command string in the open Animate document.

    Example: 'fl.trace("hello");' or 'fl.getDocumentDOM().addNewRectangle({left:0,top:0,right:100,bottom:100},0);'
    """
    result = bridge.submit("run", {"code": jsfl_command}, timeout=120.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def read_log(depth: int = 20) -> str:
    """Returns the last `depth` real logs (command logs, errors, lifecycle) from the Flash bridge.
    Loop/polling noise is filtered out."""
    result = bridge.submit("read_log", {"depth": int(depth)}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def take_screenshot() -> str:
    """Exports the current frame of the open document as a PNG saved to the flash-mcp screenshots folder
    (appdata/roaming/flash-mcp/screenshots), named HH-MM-SS-DD-MM-YYYY-screendump.png.
    Returns the saved path."""
    result = bridge.submit("take_screenshot", {}, timeout=30.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def new_keyframe(layer: int, timeline_no: int) -> str:
    """Inserts a keyframe at the given layer index and frame index (both 0-based)."""
    result = bridge.submit("new_keyframe", {"layer": int(layer), "frame": int(timeline_no)}, timeout=30.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def new_blank_keyframe(layer: int, timeline_no: int) -> str:
    """Inserts a blank keyframe at the given layer index and frame index (both 0-based)."""
    result = bridge.submit("new_blank_keyframe", {"layer": int(layer), "frame": int(timeline_no)}, timeout=30.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def select_frame(timeline_no: int) -> str:
    """Selects the frame at the given index (0-based) in the current timeline and moves the playhead there."""
    result = bridge.submit("select_frame", {"frame": int(timeline_no)}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def frame_details(timeline_no: int) -> str:
    """Reads the frame at the given index (0-based) across all layers: keyframe status, duration and element count per layer."""
    result = bridge.submit("frame_details", {"frame": int(timeline_no)}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)



@mcp.tool()
def jsfl_document_add_new_oval(boundingRectangle: str, bSuppressFill: bool, bSuppressStroke: bool) -> str:
    """(jsfl) document.addNewOval()

    Method; adds a new Oval object in the specified bounding rectangle. This method performs the same operation as the

    Args:
        boundingRectangle: str
        bSuppressFill: bool
        bSuppressStroke: bool

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().addNewOval(' + json.dumps(boundingRectangle) + ', ' + json.dumps(bSuppressFill) + ', ' + json.dumps(bSuppressStroke) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_add_new_primitive_oval(boundingRectangle: str, bSpupressFill: str, bSuppressStroke: str) -> str:
    """(jsfl) document.addNewPrimitiveOval()

    Method; adds a new oval primitive fitting into the specified bounds. This method performs the same operation as the

    Args:
        boundingRectangle: str
        bSpupressFill: str
        bSuppressStroke: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().addNewPrimitiveOval(' + json.dumps(boundingRectangle) + ', ' + json.dumps(bSpupressFill) + ', ' + json.dumps(bSuppressStroke) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_add_new_primitive_rectangle(boundingRectangle: str, roundness: str, bSuppressFill: str, bSuppressStroke: str) -> str:
    """(jsfl) document.addNewPrimitiveRectangle()

    Method; adds a new rectangle primitive fitting into the specified bounds. This method performs the same operation

    Args:
        boundingRectangle: str
        roundness: str
        bSuppressFill: str
        bSuppressStroke: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().addNewPrimitiveRectangle(' + json.dumps(boundingRectangle) + ', ' + json.dumps(roundness) + ', ' + json.dumps(bSuppressFill) + ', ' + json.dumps(bSuppressStroke) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_add_new_rectangle(boundingRectangle: str, roundness: int, bSuppressFill: bool, bSuppressStroke: bool) -> str:
    """(jsfl) document.addNewRectangle()

    Method; adds a new rectangle or rounded rectangle, fitting it into the specified bounds. This method performs the

    Args:
        boundingRectangle: str
        roundness: int
        bSuppressFill: bool
        bSuppressStroke: bool

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().addNewRectangle(' + json.dumps(boundingRectangle) + ', ' + json.dumps(roundness) + ', ' + json.dumps(bSuppressFill) + ', ' + json.dumps(bSuppressStroke) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_convert_to_symbol(type_: str, name: str, registrationPoint: str) -> str:
    """(jsfl) document.convertToSymbol()

    Method; converts the selected Stage item(s) to a new symbol. For information on defining linkage and shared asset

    Args:
        type_: str
        name: str
        registrationPoint: str
    """
    code = 'fl.getDocumentDOM().convertToSymbol(' + json.dumps(type_) + ', ' + json.dumps(name) + ', ' + json.dumps(registrationPoint) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_import_file(fileURI: str, importToLibrary: bool, showDialog: bool, showImporterUI: bool) -> str:
    """(jsfl) document.importFile()

    Method; imports a file into a document. This method performs the same operation as the Import To Library or Import

    Args:
        fileURI: str
        importToLibrary: bool
        showDialog: bool
        showImporterUI: bool

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().importFile(' + json.dumps(fileURI) + ', ' + json.dumps(importToLibrary) + ', ' + json.dumps(showDialog) + ', ' + json.dumps(showImporterUI) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_element_text_attr(attrName: str, attrValue: str, startIndex: int, endIndex: int) -> str:
    """(jsfl) document.setElementTextAttr()

    Method; sets the specified textAttrs property of the selected text items to the specified value. For a list of property

    Args:
        attrName: str
        attrValue: str
        startIndex: int
        endIndex: int

    Returns: A Boolean value: true if at least one text attribute property is changed; false otherwise.
    """
    code = 'fl.getDocumentDOM().setElementTextAttr(' + json.dumps(attrName) + ', ' + json.dumps(attrValue) + ', ' + json.dumps(startIndex) + ', ' + json.dumps(endIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_filter_property(property: str, filterIndex: int, value: str) -> str:
    """(jsfl) document.setFilterProperty()

    Method; sets a specified filter property for the currently selected objects (assuming that the object supports the

    Args:
        property: str
        filterIndex: int
        value: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setFilterProperty(' + json.dumps(property) + ', ' + json.dumps(filterIndex) + ', ' + json.dumps(value) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_selection_rect(rect: str, bReplaceCurrentSelection: str, bContactSensitiveSelection: str) -> str:
    """(jsfl) document.setSelectionRect()

    Method; draws a rectangular selection marquee relative to the Stage, using the specified coordinates. This is unlike

    Args:
        rect: str
        bReplaceCurrentSelection: str
        bContactSensitiveSelection: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setSelectionRect(' + json.dumps(rect) + ', ' + json.dumps(bReplaceCurrentSelection) + ', ' + json.dumps(bContactSensitiveSelection) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_stroke(color: str, size: float, strokeType: str) -> str:
    """(jsfl) document.setStroke()

    Method; sets the color, width, and style of the selected stroke. For information on changing the stroke in the Tools

    Args:
        color: str
        size: float
        strokeType: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setStroke(' + json.dumps(color) + ', ' + json.dumps(size) + ', ' + json.dumps(strokeType) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_text_string(text: str, startIndex: int, endIndex: int) -> str:
    """(jsfl) document.setTextString()

    Method; inserts a string of text. If the optional parameters are not passed, the existing text selection is replaced; if the

    Args:
        text: str
        startIndex: int
        endIndex: int

    Returns: A Boolean value: true if the text of at least one text string is set; false otherwise.
    """
    code = 'fl.getDocumentDOM().setTextString(' + json.dumps(text) + ', ' + json.dumps(startIndex) + ', ' + json.dumps(endIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_trace_bitmap(threshold: int, minimumArea: int, curveFit: str, cornerThreshold: str) -> str:
    """(jsfl) document.traceBitmap()

    Method; performs a trace bitmap on the current selection. This method is equivalent to selecting Modify > Bitmap >

    Args:
        threshold: int
        minimumArea: int
        curveFit: str
        cornerThreshold: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().traceBitmap(' + json.dumps(threshold) + ', ' + json.dumps(minimumArea) + ', ' + json.dumps(curveFit) + ', ' + json.dumps(cornerThreshold) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_add_item(position: str, item: str) -> str:
    """(jsfl) document.addItem()

    Method; adds an item from any open document or library to the specified Document object.

    Args:
        position: str
        item: str

    Returns: A Boolean value: true if successful; false otherwise.
    """
    code = 'fl.getDocumentDOM().addItem(' + json.dumps(position) + ', ' + json.dumps(item) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_add_new_line(startPoint: float, endpoint: float) -> str:
    """(jsfl) document.addNewLine()

    Method; adds a new path between two points. The method uses the document’s current stroke attributes and adds the

    Args:
        startPoint: float
        endpoint: float

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().addNewLine(' + json.dumps(startPoint) + ', ' + json.dumps(endpoint) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_add_new_text(boundingRectangle: str, text: str) -> str:
    """(jsfl) document.addNewText()

    Method; inserts a new text field and optionally places text into the field. If you omit the text parameter, you can call

    Args:
        boundingRectangle: str
        text: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().addNewText(' + json.dumps(boundingRectangle) + ', ' + json.dumps(text) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_align(alignmode: str, bUseDocumentBounds: bool) -> str:
    """(jsfl) document.align()

    Method; aligns the selection.

    Args:
        alignmode: str
        bUseDocumentBounds: bool

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().align(' + json.dumps(alignmode) + ', ' + json.dumps(bUseDocumentBounds) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_distribute(distributemode: str, bUseDocumentBounds: str) -> str:
    """(jsfl) document.distribute()

    Method; distributes the selection.

    Args:
        distributemode: str
        bUseDocumentBounds: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().distribute(' + json.dumps(distributemode) + ', ' + json.dumps(bUseDocumentBounds) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_export_s_w_f(fileURI: str, bCurrentSettings: bool) -> str:
    """(jsfl) document.exportSWF()

    Method; exports the document in the Flash SWF format.

    Args:
        fileURI: str
        bCurrentSettings: bool

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().exportSWF(' + json.dumps(fileURI) + ', ' + json.dumps(bCurrentSettings) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_element_property(property: str, value: int) -> str:
    """(jsfl) document.setElementProperty()

    Method; sets the specified Element property on selected objects in the document. This method does nothing if there

    Args:
        property: str
        value: int

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setElementProperty(' + json.dumps(property) + ', ' + json.dumps(value) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_instance_tint(color: str, strength: int) -> str:
    """(jsfl) document.setInstanceTint()

    Method; sets the tint for the instance.

    Args:
        color: str
        strength: int

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setInstanceTint(' + json.dumps(color) + ', ' + json.dumps(strength) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_oval_object_property(propertyName: str, value: str) -> str:
    """(jsfl) document.setOvalObjectProperty()

    Method; specifies a value for a specified property of primitive Oval objects.

    Args:
        propertyName: str
        value: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setOvalObjectProperty(' + json.dumps(propertyName) + ', ' + json.dumps(value) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_rectangle_object_property(propertyName: str, value: str) -> str:
    """(jsfl) document.setRectangleObjectProperty()

    Method; specifies a value for a specified property of primitive Rectangle objects.

    Args:
        propertyName: str
        value: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setRectangleObjectProperty(' + json.dumps(propertyName) + ', ' + json.dumps(value) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_selection_bounds(boundingRectangle: str, bContactSensitiveSelection: bool) -> str:
    """(jsfl) document.setSelectionBounds()

    Method; moves and resizes the selection in a single operation.

    Args:
        boundingRectangle: str
        bContactSensitiveSelection: bool

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setSelectionBounds(' + json.dumps(boundingRectangle) + ', ' + json.dumps(bContactSensitiveSelection) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_text_selection(startIndex: int, endIndex: int) -> str:
    """(jsfl) document.setTextSelection()

    Method; sets the text selection of the currently selected text field to the values specified by the startIndex and endIndex

    Args:
        startIndex: int
        endIndex: int

    Returns: A Boolean value: true if the method can successfully set the text selection; false otherwise.
    """
    code = 'fl.getDocumentDOM().setTextSelection(' + json.dumps(startIndex) + ', ' + json.dumps(endIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_add_filter(filterName: str) -> str:
    """(jsfl) document.addFilter()

    Method; applies a filter to the selected objects and places the filter at the end of the Filters list.

    Args:
        filterName: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().addFilter(' + json.dumps(filterName) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_remove_filter(filterIndex: int) -> str:
    """(jsfl) document.removeFilter()

    Method; removes the specified filter from the Filters list of the selected objects.

    Args:
        filterIndex: int

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().removeFilter(' + json.dumps(filterIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_rename_scene(name: str) -> str:
    """(jsfl) document.renameScene()

    Method; renames the currently selected scene in the Scenes panel. The new name for the selected scene must be unique.

    Args:
        name: str

    Returns: A Boolean value: true if the name is changed successfully; false otherwise. If the new name is not unique, for example, the method returns false.
    """
    code = 'fl.getDocumentDOM().renameScene(' + json.dumps(name) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_align_to_document(bToStage: bool) -> str:
    """(jsfl) document.setAlignToDocument()

    Method; sets the preferences for document.align(), document.distribute(), document.match(), and

    Args:
        bToStage: bool

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setAlignToDocument(' + json.dumps(bToStage) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_blend_mode(mode: str) -> str:
    """(jsfl) document.setBlendMode()

    Method; sets the blending mode for the selected objects.

    Args:
        mode: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setBlendMode(' + json.dumps(mode) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_custom_fill(fill: str) -> str:
    """(jsfl) document.setCustomFill()

    Method; sets the fill settings for the Tools panel, Property inspector, and any selected shapes. This allows a script to set

    Args:
        fill: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setCustomFill(' + json.dumps(fill) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_custom_stroke(stroke: str) -> str:
    """(jsfl) document.setCustomStroke()

    Method; sets the stroke settings for the Tools panel, Property inspector, and any selected shapes. This allows a script

    Args:
        stroke: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setCustomStroke(' + json.dumps(stroke) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_fill_color(color: str) -> str:
    """(jsfl) document.setFillColor()

    Method; changes the selection and the tools panel to the specified fill color. For additional information on changing

    Args:
        color: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setFillColor(' + json.dumps(color) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_filters(filterArray: list) -> str:
    """(jsfl) document.setFilters()

    Method; applies filters to the selected objects. Use this method after calling document.getFilters() and making any

    Args:
        filterArray: list

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setFilters(' + json.dumps(filterArray) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_instance_alpha(opacity: int) -> str:
    """(jsfl) document.setInstanceAlpha()

    Methods; sets the opacity of the instance.

    Args:
        opacity: int

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setInstanceAlpha(' + json.dumps(opacity) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_instance_brightness(brightness: int) -> str:
    """(jsfl) document.setInstanceBrightness()

    Method; sets the brightness for the instance.

    Args:
        brightness: int

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setInstanceBrightness(' + json.dumps(brightness) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_player_version(version: str) -> str:
    """(jsfl) document.setPlayerVersion()

    Method; sets the version of the Flash Player targeted by the specified document. This is the same value as that set in

    Args:
        version: str

    Returns: A value of true if the player version was successfully set; false otherwise.
    """
    code = 'fl.getDocumentDOM().setPlayerVersion(' + json.dumps(version) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_stroke_color(color: str) -> str:
    """(jsfl) document.setStrokeColor()

    Method; changes the stroke color of the selection to the specified color. For information on changing the stroke in the

    Args:
        color: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setStrokeColor(' + json.dumps(color) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_stroke_size(size: float) -> str:
    """(jsfl) document.setStrokeSize()

    Method; changes the stroke size of the selection to the specified size. For information on changing the stroke in the

    Args:
        size: float

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setStrokeSize(' + json.dumps(size) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_stroke_style(strokeType: str) -> str:
    """(jsfl) document.setStrokeStyle()

    Method; changes the stroke style of the selection to the specified style. For information on changing the stroke in the

    Args:
        strokeType: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setStrokeStyle(' + json.dumps(strokeType) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_text_rectangle(boundingRectangle: str) -> str:
    """(jsfl) document.setTextRectangle()

    Method; changes the bounding rectangle for the selected text item to the specified size. This method causes the text to

    Args:
        boundingRectangle: str

    Returns: A Boolean value: true if the size of at least one text field is changed; false otherwise.
    """
    code = 'fl.getDocumentDOM().setTextRectangle(' + json.dumps(boundingRectangle) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_set_transformation_point(transformationPoint: float) -> str:
    """(jsfl) document.setTransformationPoint()

    Method; sets the position of the current selection’s transformation point.

    Args:
        transformationPoint: float

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().setTransformationPoint(' + json.dumps(transformationPoint) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_add_new_layer(name: str, layerType: str, bAddAbove: bool) -> str:
    """(jsfl) timeline.addNewLayer()

    Method; adds a new layer to the document and makes it the current layer.

    Args:
        name: str
        layerType: str
        bAddAbove: bool

    Returns: An integer value of the zero-based index of the newly added layer.
    """
    code = 'fl.getDocumentDOM().getTimeline().addNewLayer(' + json.dumps(name) + ', ' + json.dumps(layerType) + ', ' + json.dumps(bAddAbove) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_insert_frames(numFrames: int, bAllLayers: bool, frameNumIndex: str) -> str:
    """(jsfl) timeline.insertFrames()

    Method; inserts the specified number of frames at the specified index.

    Args:
        numFrames: int
        bAllLayers: bool
        frameNumIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().insertFrames(' + json.dumps(numFrames) + ', ' + json.dumps(bAllLayers) + ', ' + json.dumps(frameNumIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_set_frame_property(property: str, value: str, startFrameIndex: str, endFrameIndex: str) -> str:
    """(jsfl) timeline.setFrameProperty()

    Method; sets the property of the Frame object for the selected frames.

    Args:
        property: str
        value: str
        startFrameIndex: str
        endFrameIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().setFrameProperty(' + json.dumps(property) + ', ' + json.dumps(value) + ', ' + json.dumps(startFrameIndex) + ', ' + json.dumps(endFrameIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_set_layer_property(property: str, value: str, layersToChange: str) -> str:
    """(jsfl) timeline.setLayerProperty()

    Method; sets the specified property on all the selected layers to a specified value.

    Args:
        property: str
        value: str
        layersToChange: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().setLayerProperty(' + json.dumps(property) + ', ' + json.dumps(value) + ', ' + json.dumps(layersToChange) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_break_apart() -> str:
    """(jsfl) document.breakApart()

    Method; performs a break-apart operation on the current selection.

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().breakApart()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_convert_lines_to_fills() -> str:
    """(jsfl) document.convertLinesToFills()

    Method; converts lines to fills on the selected objects.

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().convertLinesToFills()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_convert_selection_to_bitmap() -> str:
    """(jsfl) document.convertSelectionToBitmap()

    Method; converts selected objects in the current frame to a bitmap and inserts the bitmap into the library.

    Returns: Boolean.
    """
    code = 'fl.getDocumentDOM().convertSelectionToBitmap()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_delete_envelope() -> str:
    """(jsfl) document.deleteEnvelope()

    Method; deletes the envelope (bounding box that contains one or more objects) from the selected objects. If no objects

    Returns: None.
    """
    code = 'fl.getDocumentDOM().deleteEnvelope()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_delete_scene() -> str:
    """(jsfl) document.deleteScene()

    Method; deletes the current scene (Timeline object) and, if the deleted scene was not the last one, sets the next scene

    Returns: A Boolean value: true if the scene is successfully deleted; false otherwise.
    """
    code = 'fl.getDocumentDOM().deleteScene()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_delete_selection() -> str:
    """(jsfl) document.deleteSelection()

    Method; deletes the current selection on the Stage. Displays an error message if there is no selection.

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().deleteSelection()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_distribute_to_keyframes() -> str:
    """(jsfl) document.distributeToKeyframes()

    Method; performs a distribute-to-keyframes operation on the current selection—equivalent to selecting Distribute to

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().distributeToKeyframes()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_distribute_to_layers() -> str:
    """(jsfl) document.distributeToLayers()

    Method; performs a distribute-to-layers operation on the current selection—equivalent to selecting Distribute to

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().distributeToLayers()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_duplicate_scene() -> str:
    """(jsfl) document.duplicateScene()

    Method; makes a copy of the currently selected scene, giving the new scene a unique name and making it the current

    Returns: A Boolean value: true if the scene is duplicated successfully; false otherwise.
    """
    code = 'fl.getDocumentDOM().duplicateScene()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_duplicate_selection() -> str:
    """(jsfl) document.duplicateSelection()

    Method; duplicates the selection on the Stage.

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().duplicateSelection()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_group() -> str:
    """(jsfl) document.group()

    Method; converts the current selection to a group.

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().group()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_remove_all_filters() -> str:
    """(jsfl) document.removeAllFilters()

    Method; removes all filters from the selected objects.

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().removeAllFilters()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_convert_to_blank_keyframes(startFrameIndex: str, endFrameIndex: str) -> str:
    """(jsfl) timeline.convertToBlankKeyframes()

    Method; converts frames to blank keyframes on the current layer.

    Args:
        startFrameIndex: str
        endFrameIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().convertToBlankKeyframes(' + json.dumps(startFrameIndex) + ', ' + json.dumps(endFrameIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_convert_to_keyframes(startFrameIndex: str, endFrameIndex: str) -> str:
    """(jsfl) timeline.convertToKeyframes()

    Method; converts a range of frames to keyframes (or converts the selection if no frames are specified) on the current

    Args:
        startFrameIndex: str
        endFrameIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().convertToKeyframes(' + json.dumps(startFrameIndex) + ', ' + json.dumps(endFrameIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_copy_frames(startFrameIndex: str, endFrameIndex: str) -> str:
    """(jsfl) timeline.copyFrames()

    Method; copies a range of frames on the current layer to the clipboard.

    Args:
        startFrameIndex: str
        endFrameIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().copyFrames(' + json.dumps(startFrameIndex) + ', ' + json.dumps(endFrameIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_copy_layers(startLayerIndex: str, endLayerIndex: str) -> str:
    """(jsfl) timeline.copyLayers()

    Method; Copies the layers that are currently selected in the Timeline, or the layers in the specified range. Optional

    Args:
        startLayerIndex: str
        endLayerIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().copyLayers(' + json.dumps(startLayerIndex) + ', ' + json.dumps(endLayerIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_duplicate_layers(startLayerIndex: str, endLayerIndex: str) -> str:
    """(jsfl) timeline.duplicateLayers()

    Method; Duplicates the layers that are currently selected in the Timeline, or the layers in the specified range. Optional

    Args:
        startLayerIndex: str
        endLayerIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().duplicateLayers(' + json.dumps(startLayerIndex) + ', ' + json.dumps(endLayerIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_paste_frames(startFrameIndex: str, endFrameIndex: str) -> str:
    """(jsfl) timeline.pasteFrames()

    Method; pastes the range of frames from the clipboard into the specified frames.

    Args:
        startFrameIndex: str
        endFrameIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().pasteFrames(' + json.dumps(startFrameIndex) + ', ' + json.dumps(endFrameIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_remove_frames(startFrameIndex: str, endFrameIndex: str) -> str:
    """(jsfl) timeline.removeFrames()

    Method; deletes the frame.

    Args:
        startFrameIndex: str
        endFrameIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().removeFrames(' + json.dumps(startFrameIndex) + ', ' + json.dumps(endFrameIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_remove_motion_object(startFrame: str, endFrame: str) -> str:
    """(jsfl) timeline.removeMotionObject()

    Method; removes the motion object and converts the frame(s) back to static frames. The parameters are optional, and

    Args:
        startFrame: str
        endFrame: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().removeMotionObject(' + json.dumps(startFrame) + ', ' + json.dumps(endFrame) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_library_select_item(namePath: str, bReplaceCurrentSelection: bool, bSelect: bool) -> str:
    """(jsfl) library.selectItem()

    Method; selects a specified library item.

    Args:
        namePath: str
        bReplaceCurrentSelection: bool
        bSelect: bool

    Returns: A Boolean value: true if the specified item exists; false otherwise.
    """
    code = 'fl.getDocumentDOM().library.selectItem(' + json.dumps(namePath) + ', ' + json.dumps(bReplaceCurrentSelection) + ', ' + json.dumps(bSelect) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_delete_layer(index: str) -> str:
    """(jsfl) timeline.deleteLayer()

    Method; deletes a layer. If the layer is a folder, all layers within the folder are deleted. If you do not specify the layer

    Args:
        index: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().deleteLayer(' + json.dumps(index) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_insert_blank_keyframe(frameNumIndex: str) -> str:
    """(jsfl) timeline.insertBlankKeyframe()

    Method; inserts a blank keyframe at the specified frame index; if the index is not specified, the method inserts the blank

    Args:
        frameNumIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().insertBlankKeyframe(' + json.dumps(frameNumIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_insert_keyframe(frameNumIndex: str) -> str:
    """(jsfl) timeline.insertKeyframe()

    Method; inserts a keyframe at the specified frame. If you omit the parameter, the method inserts a keyframe using the

    Args:
        frameNumIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().insertKeyframe(' + json.dumps(frameNumIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_paste_layers(layerIndex: str) -> str:
    """(jsfl) timeline.pasteLayers()

    Method; Paste layers that have been previously cut or copied above the currently selected layer, or above the specified

    Args:
        layerIndex: str

    Returns: Integer indicating the lowest layer index of the layers that were pasted.
    """
    code = 'fl.getDocumentDOM().getTimeline().pasteLayers(' + json.dumps(layerIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_set_guidelines(xmlString: str) -> str:
    """(jsfl) timeline.setGuidelines()

    Method: replaces the guide lines for the timeline (View > Guides > Show Guides) with the information specified in

    Args:
        xmlString: str

    Returns: A Boolean value of true if the guidelines are successfully applied; false otherwise.
    """
    code = 'fl.getDocumentDOM().getTimeline().setGuidelines(' + json.dumps(xmlString) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_show_layer_masking(layer: str) -> str:
    """(jsfl) timeline.showLayerMasking()

    Method; shows the layer masking during authoring by locking the mask and masked layers. This method uses the

    Args:
        layer: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().showLayerMasking(' + json.dumps(layer) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_library_add_item_to_document(position: str, namePath: str) -> str:
    """(jsfl) library.addItemToDocument()

    Method; adds the current or specified item to the Stage at the specified position.

    Args:
        position: str
        namePath: str

    Returns: A Boolean value: true if the item is successfully added to the document; false otherwise.
    """
    code = 'fl.getDocumentDOM().library.addItemToDocument(' + json.dumps(position) + ', ' + json.dumps(namePath) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_library_add_new_item(type_: str, namePath: str) -> str:
    """(jsfl) library.addNewItem()

    library.items An array of Item objects in the library

    Args:
        type_: str
        namePath: str

    Returns: A Boolean value: true if the item is successfully created; false otherwise.
    """
    code = 'fl.getDocumentDOM().library.addNewItem(' + json.dumps(type_) + ', ' + json.dumps(namePath) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_library_set_item_property(property: str, value: str) -> str:
    """(jsfl) library.setItemProperty()

    Method; sets the property for all selected library items (ignoring folders).

    Args:
        property: str
        value: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().library.setItemProperty(' + json.dumps(property) + ', ' + json.dumps(value) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_add_motion_guide() -> str:
    """(jsfl) timeline.addMotionGuide()

    Method; adds a motion guide layer above the current layer and attaches the current layer to the newly added guide

    Returns: An integer that represents the zero-based index of the newly added guide layer. If the current layer type is not of type "Normal", Flash returns -1.
    """
    code = 'fl.getDocumentDOM().getTimeline().addMotionGuide()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_copy_motion() -> str:
    """(jsfl) timeline.copyMotion()

    Method; copies motion on selected frames, either from a motion tween or from frame-by-frame animation. You can

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().copyMotion()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_paste_motion() -> str:
    """(jsfl) timeline.pasteMotion()

    Method; pastes the range of motion frames retrieved by timeline.copyMotion() to the Timeline. If necessary,

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().pasteMotion()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_paste_motion_special() -> str:
    """(jsfl) timeline.pasteMotionSpecial()

    Method; Pastes motion on selected frames. Applies only to a copied classic tween, not a motion tween. Displays a

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().pasteMotionSpecial()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_fl_run_script(fileURI: str, funcName: str, arg1: str, arg2: str) -> str:
    """(jsfl) fl.runScript()

    Method; executes a JavaScript file. If a function is specified as one of the arguments, it runs the function and also any

    Args:
        fileURI: str
        funcName: str
        arg1: str
        arg2: str

    Returns: The function's result as a string, if funcName is specified; otherwise, nothing.
    """
    code = 'fl.runScript(' + json.dumps(fileURI) + ', ' + json.dumps(funcName) + ', ' + json.dumps(arg1) + ', ' + json.dumps(arg2) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_frame_set_custom_ease(property: str, easeCurve: str, l: int = 0, f: int = 0) -> str:
    """(jsfl) frame.setCustomEase()

    Method; specifies an array of control point and tangent endpoint coordinates that describe a cubic Bézier curve to be

    Args:
        l: index for frame (default 0)
        f: index for frame (default 0)
        property: str
        easeCurve: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().layers[' + json.dumps(l) + '].frames[' + json.dumps(f) + '].setCustomEase(' + json.dumps(property) + ', ' + json.dumps(easeCurve) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_frame_set_motion_object_duration(duration: str, stretchExistingKeyframes: str, l: int = 0, f: int = 0) -> str:
    """(jsfl) frame.setMotionObjectDuration()

    Method; sets the duration (the tween span length) of the currently selected motion object.

    Args:
        l: index for frame (default 0)
        f: index for frame (default 0)
        duration: str
        stretchExistingKeyframes: str
    """
    code = 'fl.getDocumentDOM().getTimeline().layers[' + json.dumps(l) + '].frames[' + json.dumps(f) + '].setMotionObjectDuration(' + json.dumps(duration) + ', ' + json.dumps(stretchExistingKeyframes) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_frame_set_motion_object_x_m_l(xmlstr: str, endAtCurrentLocation: bool, l: int = 0, f: int = 0) -> str:
    """(jsfl) frame.setMotionObjectXML()

    Method; applies the specified motion XML to the selected motion object.

    Args:
        l: index for frame (default 0)
        f: index for frame (default 0)
        xmlstr: str
        endAtCurrentLocation: bool
    """
    code = 'fl.getDocumentDOM().getTimeline().layers[' + json.dumps(l) + '].frames[' + json.dumps(f) + '].setMotionObjectXML(' + json.dumps(xmlstr) + ', ' + json.dumps(endAtCurrentLocation) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_library_delete_item(namePath: str) -> str:
    """(jsfl) library.deleteItem()

    Method; deletes the current items or a specified item from the Library panel. This method can affect multiple items if

    Args:
        namePath: str

    Returns: A Boolean value: true if the items are successfully deleted; false otherwise.
    """
    code = 'fl.getDocumentDOM().library.deleteItem(' + json.dumps(namePath) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_library_duplicate_item(namePath: str) -> str:
    """(jsfl) library.duplicateItem()

    Method; makes a copy of the currently selected or specified item. The new item has a default name (such as item copy)

    Args:
        namePath: str

    Returns: A Boolean value: true if the item is duplicated successfully; false otherwise. If more than one item is selected, Flash returns false.
    """
    code = 'fl.getDocumentDOM().library.duplicateItem(' + json.dumps(namePath) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_library_edit_item(namePath: str) -> str:
    """(jsfl) library.editItem()

    Method; opens the currently selected or specified item in Edit mode.

    Args:
        namePath: str

    Returns: A Boolean value: true if the specified item exists and can be edited; false otherwise.
    """
    code = 'fl.getDocumentDOM().library.editItem(' + json.dumps(namePath) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_library_new_folder(folderPath: str) -> str:
    """(jsfl) library.newFolder()

    Method; creates a new folder with the specified name, or a default name ("untitled folder #") if no folderName

    Args:
        folderPath: str

    Returns: A Boolean value: true if folder is created successfully; false otherwise.
    """
    code = 'fl.getDocumentDOM().library.newFolder(' + json.dumps(folderPath) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_library_rename_item(name: str) -> str:
    """(jsfl) library.renameItem()

    Method; renames the currently selected library item in the Library panel.

    Args:
        name: str

    Returns: A Boolean value of true if the name of the item changes successfully, false otherwise. If multiple items are selected, no names are changed, and the return value is false (to match user interface behavior).
    """
    code = 'fl.getDocumentDOM().library.renameItem(' + json.dumps(name) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_library_select_all(bSelectAll: bool) -> str:
    """(jsfl) library.selectAll()

    Method; selects or deselects all items in the library.

    Args:
        bSelectAll: bool

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().library.selectAll(' + json.dumps(bSelectAll) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_fl_copy_library_item(fileURI: str, libraryItemPath: str) -> str:
    """(jsfl) fl.copyLibraryItem()

    Method; silently copies a library item from a document without exposing the item in the Flash Pro user interface. Call

    Args:
        fileURI: str
        libraryItemPath: str

    Returns: A Boolean value: true if the copy succeeds; false otherwise.
    """
    code = 'fl.copyLibraryItem(' + json.dumps(fileURI) + ', ' + json.dumps(libraryItemPath) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_fl_select_element(elementObject: bool, editMode: str) -> str:
    """(jsfl) fl.selectElement()

    Method; enables selection or editing of an element. Generally, you will use this method on objects returned by

    Args:
        elementObject: bool
        editMode: str

    Returns: A Boolean value of true if the element was successfully selected; false otherwise.
    """
    code = 'fl.selectElement(' + json.dumps(elementObject) + ', ' + json.dumps(editMode) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_fl_set_active_window(document: str, bActivateFrame: str) -> str:
    """(jsfl) fl.setActiveWindow()

    Method; sets the active window to be the specified document. This method is also supported by Dreamweaver and

    Args:
        document: str
        bActivateFrame: str

    Returns: Nothing.
    """
    code = 'fl.setActiveWindow(' + json.dumps(document) + ', ' + json.dumps(bActivateFrame) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_library_select_none() -> str:
    """(jsfl) library.selectNone()

    Method; deselects all the library items.

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().library.selectNone()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_fl_select_tool(toolName: str) -> str:
    """(jsfl) fl.selectTool()

    Method; selects the specified tool in the Tools panel. The acceptable default values for toolName are "arrow",

    Args:
        toolName: str
    """
    code = 'fl.selectTool(' + json.dumps(toolName) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_fl_trace(message: str) -> str:
    """(jsfl) fl.trace()

    Method; sends a text string to the Output panel, terminated by a new line, and displays the Output panel if it is not

    Args:
        message: str

    Returns: Nothing.
    """
    code = 'fl.trace(' + json.dumps(message) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_frame_convert_motion_object_to2_d(l: int = 0, f: int = 0) -> str:
    """(jsfl) frame.convertMotionObjectTo2D()

    Method; Converts the selected motion object to a 2D motion object.

    Args:
        l: index for frame (default 0)
        f: index for frame (default 0)
    """
    code = 'fl.getDocumentDOM().getTimeline().layers[' + json.dumps(l) + '].frames[' + json.dumps(f) + '].convertMotionObjectTo2D()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_frame_convert_motion_object_to3_d(l: int = 0, f: int = 0) -> str:
    """(jsfl) frame.convertMotionObjectTo3D()

    Method; Converts the selected motion object to a 3D motion object.

    Args:
        l: index for frame (default 0)
        f: index for frame (default 0)
    """
    code = 'fl.getDocumentDOM().getTimeline().layers[' + json.dumps(l) + '].frames[' + json.dumps(f) + '].convertMotionObjectTo3D()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_frame_convert_to_frame_by_frame_animation(l: int = 0, f: int = 0) -> str:
    """(jsfl) frame.convertToFrameByFrameAnimation()

    Method; Converts the current frame to Frame-by-Frame Animation.

    Args:
        l: index for frame (default 0)
        f: index for frame (default 0)

    Returns: Returns boolean. Returns true if the frame contains animation that can be converted to frame by frame animation. For example: return true for Motion Tween frame or Classic Tween frame; return false for other type of frame such as static.
    """
    code = 'fl.getDocumentDOM().getTimeline().layers[' + json.dumps(l) + '].frames[' + json.dumps(f) + '].convertToFrameByFrameAnimation()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_symbol_item_export_to_p_n_g_sequence(outputURI: str, startFrameNum: int, endFrameNum: int, matrix: str, i: int = 0) -> str:
    """(jsfl) symbolItem.exportToPNGSequence()

    Method; exports a movie clip, graphic, or button symbol to a sequence of PNG files on disk.

    Args:
        i: index for symbolItem (default 0)
        outputURI: str
        startFrameNum: int
        endFrameNum: int
        matrix: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().library.items[' + json.dumps(i) + '].exportToPNGSequence(' + json.dumps(outputURI) + ', ' + json.dumps(startFrameNum) + ', ' + json.dumps(endFrameNum) + ', ' + json.dumps(matrix) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_text_set_text_attr(attrName: str, attrValue: str, startIndex: str, endIndex: str, i: int = 0) -> str:
    """(jsfl) text.setTextAttr()

    Method; sets the attribute specified by the attrName parameter associated with the text identified by startIndex and

    Args:
        i: index for text (default 0)
        attrName: str
        attrValue: str
        startIndex: str
        endIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().selection[' + json.dumps(i) + '].setTextAttr(' + json.dumps(attrName) + ', ' + json.dumps(attrValue) + ', ' + json.dumps(startIndex) + ', ' + json.dumps(endIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_text_set_text_string(text: str, startIndex: str, endIndex: str, i: int = 0) -> str:
    """(jsfl) text.setTextString()

    Property; changes the text string within this Text object. If you omit the optional parameters, the whole Text object is

    Args:
        i: index for text (default 0)
        text: str
        startIndex: str
        endIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().selection[' + json.dumps(i) + '].setTextString(' + json.dumps(text) + ', ' + json.dumps(startIndex) + ', ' + json.dumps(endIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_element_set_transformation_point(transformationPoint: float, i: int = 0) -> str:
    """(jsfl) element.setTransformationPoint()

    Method; sets the position of the element’s transformation point.

    Args:
        i: index for element (default 0)
        transformationPoint: float

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().selection[' + json.dumps(i) + '].setTransformationPoint(' + json.dumps(transformationPoint) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_sprite_sheet_exporter_add_symbol(symbol: str, name: str, beginFrame: str, endFrame: str) -> str:
    """(jsfl) SpriteSheetExporter.addSymbol()

    Method; Adds the specified SymbolItem or SymbolInstance to be used to generate the sprite sheet.

    Args:
        symbol: str
        name: str
        beginFrame: str
        endFrame: str

    Returns: Boolean.
    """
    code = 'new SpriteSheetExporter.addSymbol(' + json.dumps(symbol) + ', ' + json.dumps(name) + ', ' + json.dumps(beginFrame) + ', ' + json.dumps(endFrame) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_sprite_sheet_exporter_export_sprite_sheet(path: str, imageFormat: str, writeMetaData: bool) -> str:
    """(jsfl) SpriteSheetExporter.exportSpriteSheet()

    Method; Exports the sprite sheet into a an image file and a metadata file based on the path parameter. The return string

    Args:
        path: str
        imageFormat: str
        writeMetaData: bool

    Returns: String.
    """
    code = 'new SpriteSheetExporter.exportSpriteSheet(' + json.dumps(path) + ', ' + json.dumps(imageFormat) + ', ' + json.dumps(writeMetaData) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_symbol_item_export_to_library(frameNumber: int, bitmapName: str, i: int = 0) -> str:
    """(jsfl) symbolItem.exportToLibrary()

    Method; exports a frame from the selected instance of movie clip, graphic, or button symbol on the Stage to a bitmap

    Args:
        i: index for symbolItem (default 0)
        frameNumber: int
        bitmapName: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().library.items[' + json.dumps(i) + '].exportToLibrary(' + json.dumps(frameNumber) + ', ' + json.dumps(bitmapName) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_bitmap_item_export_to_file(fileURI: str, quality: str, i: int = 0) -> str:
    """(jsfl) bitmapItem.exportToFile()

    Method; exports the specified item to a PNG or JPG file.

    Args:
        i: index for bitmapItem (default 0)
        fileURI: str
        quality: str

    Returns: A Boolean value of true if the file was exported successfully; false otherwise.
    """
    code = 'fl.getDocumentDOM().library.items[' + json.dumps(i) + '].exportToFile(' + json.dumps(fileURI) + ', ' + json.dumps(quality) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_symbol_item_export_s_w_f(outputURI: str, i: int = 0) -> str:
    """(jsfl) symbolItem.exportSWF()

    Method; exports the symbol item to a SWF file.

    Args:
        i: index for symbolItem (default 0)
        outputURI: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().library.items[' + json.dumps(i) + '].exportSWF(' + json.dumps(outputURI) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_path_add_cubic_curve(xAnchor: float, yAnchor: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> str:
    """(jsfl) path.addCubicCurve()

    path.addCubicCurve() Appends a cubic Bézier curve segment to the path.

    Args:
        xAnchor: float
        yAnchor: float
        x2: float
        y2: float
        x3: float
        y3: float
        x4: float
        y4: float

    Returns: Nothing.
    """
    code = 'fl.drawingLayer.newPath().addCubicCurve(' + json.dumps(xAnchor) + ', ' + json.dumps(yAnchor) + ', ' + json.dumps(x2) + ', ' + json.dumps(y2) + ', ' + json.dumps(x3) + ', ' + json.dumps(y3) + ', ' + json.dumps(x4) + ', ' + json.dumps(y4) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_path_add_curve(xAnchor: float, yAnchor: float, x2: float, y2: float, x3: float, y3: float) -> str:
    """(jsfl) path.addCurve()

    Method; appends a quadratic Bézier segment to the path.

    Args:
        xAnchor: float
        yAnchor: float
        x2: float
        y2: float
        x3: float
        y3: float

    Returns: Nothing.
    """
    code = 'fl.drawingLayer.newPath().addCurve(' + json.dumps(xAnchor) + ', ' + json.dumps(yAnchor) + ', ' + json.dumps(x2) + ', ' + json.dumps(y2) + ', ' + json.dumps(x3) + ', ' + json.dumps(y3) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_shape_delete_edge(index: str, i: int = 0) -> str:
    """(jsfl) shape.deleteEdge()

    Method; deletes the specified edge. You must call shape.beginEdit() before using this method.

    Args:
        i: index for shape (default 0)
        index: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().selection[' + json.dumps(i) + '].deleteEdge(' + json.dumps(index) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_edge_set_control(index: int, x: float, y: float, i: int = 0, j: int = 0) -> str:
    """(jsfl) edge.setControl()

    Method; sets the position of the control point of the edge. You must call shape.beginEdit() before using this

    Args:
        i: index for edge (default 0)
        j: index for edge (default 0)
        index: int
        x: float
        y: float

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().selection[' + json.dumps(i) + '].edges[' + json.dumps(j) + '].setControl(' + json.dumps(index) + ', ' + json.dumps(x) + ', ' + json.dumps(y) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_sound_item_export_to_file(fileURI: str, i: int = 0) -> str:
    """(jsfl) soundItem.exportToFile()

    Method; exports the specified item to a WAV or MP3 file. Export settings are based on the item being exported.

    Args:
        i: index for soundItem (default 0)
        fileURI: str

    Returns: A Boolean value of true if the file was exported successfully; false otherwise.
    """
    code = 'fl.getDocumentDOM().library.items[' + json.dumps(i) + '].exportToFile(' + json.dumps(fileURI) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_expand_folder(bExpand: bool, bRecurseNestedParents: bool, index: str) -> str:
    """(jsfl) timeline.expandFolder()

    Method; expands or collapses the specified folder or folders. If you do not specify a layer, this method operates on the

    Args:
        bExpand: bool
        bRecurseNestedParents: bool
        index: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().expandFolder(' + json.dumps(bExpand) + ', ' + json.dumps(bRecurseNestedParents) + ', ' + json.dumps(index) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_f_lfile_copy(fileURI: str, copyURI: str) -> str:
    """(jsfl) FLfile.copy()

    Method; copies a file from one location to another. This method returns false if copyURI already exists.

    Args:
        fileURI: str
        copyURI: str

    Returns: A Boolean value of true if successful; false otherwise.
    """
    code = 'FLfile.copy(' + json.dumps(fileURI) + ', ' + json.dumps(copyURI) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_f_lfile_list_folder(folderURI: str, filesOrDirectories: str) -> str:
    """(jsfl) FLfile.listFolder()

    Method; returns an array of strings representing the contents of the folder.

    Args:
        folderURI: str
        filesOrDirectories: str

    Returns: An array of strings representing the contents of the folder. If the folder doesn’t exist or if no files or folders match the specified criteria, returns an empty array.
    """
    code = 'FLfile.listFolder(' + json.dumps(folderURI) + ', ' + json.dumps(filesOrDirectories) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_vertex_set_location(x: float, y: float, i: int = 0, j: int = 0, h: int = 0) -> str:
    """(jsfl) vertex.setLocation()

    Method; sets the location of the vertex. You must call shape.beginEdit() before using this method.

    Args:
        i: index for vertex (default 0)
        j: index for vertex (default 0)
        h: index for vertex (default 0)
        x: float
        y: float

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().selection[' + json.dumps(i) + '].edges[' + json.dumps(j) + '].getHalfEdge(' + json.dumps(h) + ').getVertex().setLocation(' + json.dumps(x) + ', ' + json.dumps(y) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_output_panel_trace(message: str) -> str:
    """(jsfl) outputPanel.trace()

    Method; sends a text string to the Output panel, terminated by a new line, and displays the Output panel if it is not

    Args:
        message: str

    Returns: Nothing.
    """
    code = 'fl.outputPanel.trace(' + json.dumps(message) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_clear_frames(startFrameIndex: str, endFrameIndex: str) -> str:
    """(jsfl) timeline.clearFrames()

    Method; deletes all the contents from a frame or range of frames on the current layer.

    Args:
        startFrameIndex: str
        endFrameIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().clearFrames(' + json.dumps(startFrameIndex) + ', ' + json.dumps(endFrameIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_clear_keyframes(startFrameIndex: str, endFrameIndex: str) -> str:
    """(jsfl) timeline.clearKeyframes()

    Method; converts a keyframe to a regular frame and deletes its contents on the current layer.

    Args:
        startFrameIndex: str
        endFrameIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().clearKeyframes(' + json.dumps(startFrameIndex) + ', ' + json.dumps(endFrameIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_create_motion_object(startFrame: str, endFrame: str) -> str:
    """(jsfl) timeline.createMotionObject()

    Method; creates a new motion object. The parameters are optional, and if specified set the timeline selection to the

    Args:
        startFrame: str
        endFrame: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().createMotionObject(' + json.dumps(startFrame) + ', ' + json.dumps(endFrame) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_create_motion_tween(startFrameIndex: str, endFrameIndex: str) -> str:
    """(jsfl) timeline.createMotionTween()

    Method; sets the frame.tweenType property to motion for each selected keyframe on the current layer, and converts

    Args:
        startFrameIndex: str
        endFrameIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().createMotionTween(' + json.dumps(startFrameIndex) + ', ' + json.dumps(endFrameIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_cut_frames(startFrameIndex: str, endFrameIndex: str) -> str:
    """(jsfl) timeline.cutFrames()

    Method; cuts a range of frames on the current layer from the timeline and saves them to the clipboard.

    Args:
        startFrameIndex: str
        endFrameIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().cutFrames(' + json.dumps(startFrameIndex) + ', ' + json.dumps(endFrameIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_cut_layers(startLayerIndex: str, endLayerIndex: str) -> str:
    """(jsfl) timeline.cutLayers()

    Method; Cuts the layers that are currently selected in the Timeline, or the layers in the specified range. Optional

    Args:
        startLayerIndex: str
        endLayerIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().cutLayers(' + json.dumps(startLayerIndex) + ', ' + json.dumps(endLayerIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_reverse_frames(startFrameIndex: str, endFrameIndex: str) -> str:
    """(jsfl) timeline.reverseFrames()

    Method; reverses a range of frames.

    Args:
        startFrameIndex: str
        endFrameIndex: str

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().reverseFrames(' + json.dumps(startFrameIndex) + ', ' + json.dumps(endFrameIndex) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_library_move_to_folder(folderPath: str, itemToMove: str, bReplace: bool) -> str:
    """(jsfl) library.moveToFolder()

    Method; moves the currently selected or specified library item to a specified folder. If the folderPath parameter is

    Args:
        folderPath: str
        itemToMove: str
        bReplace: bool

    Returns: A Boolean value: true if the item moves successfully; false otherwise.
    """
    code = 'fl.getDocumentDOM().library.moveToFolder(' + json.dumps(folderPath) + ', ' + json.dumps(itemToMove) + ', ' + json.dumps(bReplace) + ')'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_start_playback() -> str:
    """(jsfl) timeline.startPlayback()

    Method; starts automatic playback of the timeline if it is currently playing. This method can be used with SWF panels

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().startPlayback()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_stop_playback() -> str:
    """(jsfl) timeline.stopPlayback()

    Method; stops automatic playback of the timeline if it is currently playing. This method can be used with SWF panels

    Returns: Nothing.
    """
    code = 'fl.getDocumentDOM().getTimeline().stopPlayback()'
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_f_lfile_state(operation: str = "getAttributes", params: str = "{}") -> str:
    """(jsfl) FLfile.* state/query commands (merged tool)

    Pick one operation; supply its arguments as a JSON string in `params`.

    Args:
        operation: getAttributes, getCreationDate, getCreationDateObj, getModificationDate, getModificationDateObj, getSize
        params: JSON object of the operation's arguments, e.g. '{"fileURI": "file:///C:/x.fla"}'.

    Supported operations:
        - getAttributes(fileOrFolderURI)
        - getCreationDate(fileOrFolderURI)
        - getCreationDateObj(fileOrFolderURI)
        - getModificationDate(fileOrFolderURI)
        - getModificationDateObj(fileOrFolderURI)
        - getSize(fileURI)
    """
    p = json.loads(params) if params else {}
    if operation == 'getAttributes':
        code = ('FLfile') + '.getAttributes(' + json.dumps(p.get('fileOrFolderURI')) + ')'
    elif operation == 'getCreationDate':
        code = ('FLfile') + '.getCreationDate(' + json.dumps(p.get('fileOrFolderURI')) + ')'
    elif operation == 'getCreationDateObj':
        code = ('FLfile') + '.getCreationDateObj(' + json.dumps(p.get('fileOrFolderURI')) + ')'
    elif operation == 'getModificationDate':
        code = ('FLfile') + '.getModificationDate(' + json.dumps(p.get('fileOrFolderURI')) + ')'
    elif operation == 'getModificationDateObj':
        code = ('FLfile') + '.getModificationDateObj(' + json.dumps(p.get('fileOrFolderURI')) + ')'
    elif operation == 'getSize':
        code = ('FLfile') + '.getSize(' + json.dumps(p.get('fileURI')) + ')'
    else:
        return json.dumps({"ok": False, "error": "unknown operation: " + operation}, ensure_ascii=False)
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_tween_state(operation: str = "getGeometricTransform", params: str = "{}") -> str:
    """(jsfl) Tween.* state/query commands (merged tool)

    Pick one operation; supply its arguments as a JSON string in `params`.

    Args:
        operation: getGeometricTransform
        params: JSON object of the operation's arguments, e.g. '{"fileURI": "file:///C:/x.fla"}'.

    Supported operations:
        - getGeometricTransform(frameIndex)
    """
    p = json.loads(params) if params else {}
    if operation == 'getGeometricTransform':
        code = ('fl.getDocumentDOM().getTimeline().layers[' + json.dumps(p.get('l', 0)) + '].frames[' + json.dumps(p.get('f', 0)) + '].tweenObj') + '.getGeometricTransform(' + json.dumps(p.get('frameIndex')) + ')'
    else:
        return json.dumps({"ok": False, "error": "unknown operation: " + operation}, ensure_ascii=False)
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_bitmap_instance_state(operation: str = "getBits", params: str = "{}") -> str:
    """(jsfl) bitmapInstance.* state/query commands (merged tool)

    Pick one operation; supply its arguments as a JSON string in `params`.

    Args:
        operation: getBits
        params: JSON object of the operation's arguments, e.g. '{"fileURI": "file:///C:/x.fla"}'.

    Supported operations:
        - getBits()
    """
    p = json.loads(params) if params else {}
    if operation == 'getBits':
        code = ('fl.getDocumentDOM().selection[' + json.dumps(p.get('i', 0)) + ']') + '.getBits()'
    else:
        return json.dumps({"ok": False, "error": "unknown operation: " + operation}, ensure_ascii=False)
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_document_state(operation: str = "addNewScene", params: str = "{}") -> str:
    """(jsfl) document.* state/query commands (merged tool)

    Pick one operation; supply its arguments as a JSON string in `params`.

    Args:
        operation: addNewScene, canEditSymbol, canRevert, canTestMovie, canTestScene, close, debugMovie, documentHasData, editScene, exportInstanceToLibrary, exportInstanceToPNGSequence, exportPNG, getAlignToDocument, getBlendMode, getCustomFill, getCustomStroke, getDataFromDocument, getElementProperty, getElementTextAttr, getFilters, getMetadata, getMobileSettings, getPlayerVersion, getPublishDocumentData, getSWFPathFromProfile, getSelectionRect, getTelemetryForSwf, getTextString, getTimeline, getTransformationPoint, publish, revert, save, saveAsCopy, testMovie, testScene
        params: JSON object of the operation's arguments, e.g. '{"fileURI": "file:///C:/x.fla"}'.

    Supported operations:
        - addNewScene(name)
        - canEditSymbol()
        - canRevert()
        - canTestMovie()
        - canTestScene()
        - close(bPromptToSaveChanges)
        - debugMovie(Boolean)
        - documentHasData(name)
        - editScene(index)
        - exportInstanceToLibrary(frameNumber, bitmapName)
        - exportInstanceToPNGSequence(outputURI, startFrameNum, endFrameNum, matrix)
        - exportPNG(fileURI, bCurrentPNGSettings, bCurrentFrame)
        - getAlignToDocument()
        - getBlendMode()
        - getCustomFill(objectToFill)
        - getCustomStroke(locationOfStroke)
        - getDataFromDocument(name)
        - getElementProperty(propertyName)
        - getElementTextAttr(attrName, startIndex, endIndex)
        - getFilters()
        - getMetadata()
        - getMobileSettings()
        - getPlayerVersion()
        - getPublishDocumentData(format)
        - getSWFPathFromProfile()
        - getSelectionRect()
        - getTelemetryForSwf()
        - getTextString(startIndex, endIndex)
        - getTimeline()
        - getTransformationPoint()
        - publish()
        - revert()
        - save(bOkToSaveAs)
        - saveAsCopy(URI, selectionOnly)
        - testMovie(Boolean)
        - testScene()
    """
    p = json.loads(params) if params else {}
    if operation == 'addNewScene':
        code = ('fl.getDocumentDOM()') + '.addNewScene(' + json.dumps(p.get('name')) + ')'
    elif operation == 'canEditSymbol':
        code = ('fl.getDocumentDOM()') + '.canEditSymbol()'
    elif operation == 'canRevert':
        code = ('fl.getDocumentDOM()') + '.canRevert()'
    elif operation == 'canTestMovie':
        code = ('fl.getDocumentDOM()') + '.canTestMovie()'
    elif operation == 'canTestScene':
        code = ('fl.getDocumentDOM()') + '.canTestScene()'
    elif operation == 'close':
        code = ('fl.getDocumentDOM()') + '.close(' + json.dumps(p.get('bPromptToSaveChanges')) + ')'
    elif operation == 'debugMovie':
        code = ('fl.getDocumentDOM()') + '.debugMovie(' + json.dumps(p.get('Boolean')) + ')'
    elif operation == 'documentHasData':
        code = ('fl.getDocumentDOM()') + '.documentHasData(' + json.dumps(p.get('name')) + ')'
    elif operation == 'editScene':
        code = ('fl.getDocumentDOM()') + '.editScene(' + json.dumps(p.get('index')) + ')'
    elif operation == 'exportInstanceToLibrary':
        code = ('fl.getDocumentDOM()') + '.exportInstanceToLibrary(' + json.dumps(p.get('frameNumber')) + ', ' + json.dumps(p.get('bitmapName')) + ')'
    elif operation == 'exportInstanceToPNGSequence':
        code = ('fl.getDocumentDOM()') + '.exportInstanceToPNGSequence(' + json.dumps(p.get('outputURI')) + ', ' + json.dumps(p.get('startFrameNum')) + ', ' + json.dumps(p.get('endFrameNum')) + ', ' + json.dumps(p.get('matrix')) + ')'
    elif operation == 'exportPNG':
        code = ('fl.getDocumentDOM()') + '.exportPNG(' + json.dumps(p.get('fileURI')) + ', ' + json.dumps(p.get('bCurrentPNGSettings')) + ', ' + json.dumps(p.get('bCurrentFrame')) + ')'
    elif operation == 'getAlignToDocument':
        code = ('fl.getDocumentDOM()') + '.getAlignToDocument()'
    elif operation == 'getBlendMode':
        code = ('fl.getDocumentDOM()') + '.getBlendMode()'
    elif operation == 'getCustomFill':
        code = ('fl.getDocumentDOM()') + '.getCustomFill(' + json.dumps(p.get('objectToFill')) + ')'
    elif operation == 'getCustomStroke':
        code = ('fl.getDocumentDOM()') + '.getCustomStroke(' + json.dumps(p.get('locationOfStroke')) + ')'
    elif operation == 'getDataFromDocument':
        code = ('fl.getDocumentDOM()') + '.getDataFromDocument(' + json.dumps(p.get('name')) + ')'
    elif operation == 'getElementProperty':
        code = ('fl.getDocumentDOM()') + '.getElementProperty(' + json.dumps(p.get('propertyName')) + ')'
    elif operation == 'getElementTextAttr':
        code = ('fl.getDocumentDOM()') + '.getElementTextAttr(' + json.dumps(p.get('attrName')) + ', ' + json.dumps(p.get('startIndex')) + ', ' + json.dumps(p.get('endIndex')) + ')'
    elif operation == 'getFilters':
        code = ('fl.getDocumentDOM()') + '.getFilters()'
    elif operation == 'getMetadata':
        code = ('fl.getDocumentDOM()') + '.getMetadata()'
    elif operation == 'getMobileSettings':
        code = ('fl.getDocumentDOM()') + '.getMobileSettings()'
    elif operation == 'getPlayerVersion':
        code = ('fl.getDocumentDOM()') + '.getPlayerVersion()'
    elif operation == 'getPublishDocumentData':
        code = ('fl.getDocumentDOM()') + '.getPublishDocumentData(' + json.dumps(p.get('format')) + ')'
    elif operation == 'getSWFPathFromProfile':
        code = ('fl.getDocumentDOM()') + '.getSWFPathFromProfile()'
    elif operation == 'getSelectionRect':
        code = ('fl.getDocumentDOM()') + '.getSelectionRect()'
    elif operation == 'getTelemetryForSwf':
        code = ('fl.getDocumentDOM()') + '.getTelemetryForSwf()'
    elif operation == 'getTextString':
        code = ('fl.getDocumentDOM()') + '.getTextString(' + json.dumps(p.get('startIndex')) + ', ' + json.dumps(p.get('endIndex')) + ')'
    elif operation == 'getTimeline':
        code = ('fl.getDocumentDOM()') + '.getTimeline()'
    elif operation == 'getTransformationPoint':
        code = ('fl.getDocumentDOM()') + '.getTransformationPoint()'
    elif operation == 'publish':
        code = ('fl.getDocumentDOM()') + '.publish()'
    elif operation == 'revert':
        code = ('fl.getDocumentDOM()') + '.revert()'
    elif operation == 'save':
        code = ('fl.getDocumentDOM()') + '.save(' + json.dumps(p.get('bOkToSaveAs')) + ')'
    elif operation == 'saveAsCopy':
        code = ('fl.getDocumentDOM()') + '.saveAsCopy(' + json.dumps(p.get('URI')) + ', ' + json.dumps(p.get('selectionOnly')) + ')'
    elif operation == 'testMovie':
        code = ('fl.getDocumentDOM()') + '.testMovie(' + json.dumps(p.get('Boolean')) + ')'
    elif operation == 'testScene':
        code = ('fl.getDocumentDOM()') + '.testScene()'
    else:
        return json.dumps({"ok": False, "error": "unknown operation: " + operation}, ensure_ascii=False)
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_edge_state(operation: str = "getControl", params: str = "{}") -> str:
    """(jsfl) edge.* state/query commands (merged tool)

    Pick one operation; supply its arguments as a JSON string in `params`.

    Args:
        operation: getControl, getHalfEdge
        params: JSON object of the operation's arguments, e.g. '{"fileURI": "file:///C:/x.fla"}'.

    Supported operations:
        - getControl(i)
        - getHalfEdge(index)
    """
    p = json.loads(params) if params else {}
    if operation == 'getControl':
        code = ('fl.getDocumentDOM().selection[' + json.dumps(p.get('i', 0)) + '].edges[' + json.dumps(p.get('j', 0)) + ']') + '.getControl(' + json.dumps(p.get('i')) + ')'
    elif operation == 'getHalfEdge':
        code = ('fl.getDocumentDOM().selection[' + json.dumps(p.get('i', 0)) + '].edges[' + json.dumps(p.get('j', 0)) + ']') + '.getHalfEdge(' + json.dumps(p.get('index')) + ')'
    else:
        return json.dumps({"ok": False, "error": "unknown operation: " + operation}, ensure_ascii=False)
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_element_state(operation: str = "getPersistentData", params: str = "{}") -> str:
    """(jsfl) element.* state/query commands (merged tool)

    Pick one operation; supply its arguments as a JSON string in `params`.

    Args:
        operation: getPersistentData, getPublishPersistentData, getTransformationPoint, hasPersistentData
        params: JSON object of the operation's arguments, e.g. '{"fileURI": "file:///C:/x.fla"}'.

    Supported operations:
        - getPersistentData(name)
        - getPublishPersistentData(name, format)
        - getTransformationPoint()
        - hasPersistentData(name)
    """
    p = json.loads(params) if params else {}
    if operation == 'getPersistentData':
        code = ('fl.getDocumentDOM().selection[' + json.dumps(p.get('i', 0)) + ']') + '.getPersistentData(' + json.dumps(p.get('name')) + ')'
    elif operation == 'getPublishPersistentData':
        code = ('fl.getDocumentDOM().selection[' + json.dumps(p.get('i', 0)) + ']') + '.getPublishPersistentData(' + json.dumps(p.get('name')) + ', ' + json.dumps(p.get('format')) + ')'
    elif operation == 'getTransformationPoint':
        code = ('fl.getDocumentDOM().selection[' + json.dumps(p.get('i', 0)) + ']') + '.getTransformationPoint()'
    elif operation == 'hasPersistentData':
        code = ('fl.getDocumentDOM().selection[' + json.dumps(p.get('i', 0)) + ']') + '.hasPersistentData(' + json.dumps(p.get('name')) + ')'
    else:
        return json.dumps({"ok": False, "error": "unknown operation: " + operation}, ensure_ascii=False)
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_fl_state(operation: str = "closeAll", params: str = "{}") -> str:
    """(jsfl) fl.* state/query commands (merged tool)

    Pick one operation; supply its arguments as a JSON string in `params`.

    Args:
        operation: closeAll, closeAllPlayerDocuments, closeDocument, findDocumentDOM, findDocumentIndex, findObjectInDocByName, findObjectInDocByType, getAppMemoryInfo, getDocumentDOM, getSwfPanel, getThemeColor, getThemeColorParameters, getThemeFontInfo, isFontInstalled, openDocument, openScript, publishDocument, revertDocument, saveAll, saveDocument, saveDocumentAs
        params: JSON object of the operation's arguments, e.g. '{"fileURI": "file:///C:/x.fla"}'.

    Supported operations:
        - closeAll(bPromptToSave)
        - closeAllPlayerDocuments()
        - closeDocument(documentObject, bPromptToSaveChanges)
        - findDocumentDOM(id)
        - findDocumentIndex(name)
        - findObjectInDocByName(instanceName, document)
        - findObjectInDocByType(elementType, document)
        - getAppMemoryInfo(memType)
        - getDocumentDOM()
        - getSwfPanel(panelName, useLocalizedPanelName)
        - getThemeColor(themeParamName)
        - getThemeColorParameters()
        - getThemeFontInfo(infoType, size)
        - isFontInstalled(fontName)
        - openDocument(fileURI)
        - openScript(fileURI)
        - publishDocument(flaURI, publishProfile)
        - revertDocument(documentObject)
        - saveAll()
        - saveDocument(document, fileURI)
        - saveDocumentAs(document)
    """
    p = json.loads(params) if params else {}
    if operation == 'closeAll':
        code = ('fl') + '.closeAll(' + json.dumps(p.get('bPromptToSave')) + ')'
    elif operation == 'closeAllPlayerDocuments':
        code = ('fl') + '.closeAllPlayerDocuments()'
    elif operation == 'closeDocument':
        code = ('fl') + '.closeDocument(' + json.dumps(p.get('documentObject')) + ', ' + json.dumps(p.get('bPromptToSaveChanges')) + ')'
    elif operation == 'findDocumentDOM':
        code = ('fl') + '.findDocumentDOM(' + json.dumps(p.get('id')) + ')'
    elif operation == 'findDocumentIndex':
        code = ('fl') + '.findDocumentIndex(' + json.dumps(p.get('name')) + ')'
    elif operation == 'findObjectInDocByName':
        code = ('fl') + '.findObjectInDocByName(' + json.dumps(p.get('instanceName')) + ', ' + json.dumps(p.get('document')) + ')'
    elif operation == 'findObjectInDocByType':
        code = ('fl') + '.findObjectInDocByType(' + json.dumps(p.get('elementType')) + ', ' + json.dumps(p.get('document')) + ')'
    elif operation == 'getAppMemoryInfo':
        code = ('fl') + '.getAppMemoryInfo(' + json.dumps(p.get('memType')) + ')'
    elif operation == 'getDocumentDOM':
        code = ('fl') + '.getDocumentDOM()'
    elif operation == 'getSwfPanel':
        code = ('fl') + '.getSwfPanel(' + json.dumps(p.get('panelName')) + ', ' + json.dumps(p.get('useLocalizedPanelName')) + ')'
    elif operation == 'getThemeColor':
        code = ('fl') + '.getThemeColor(' + json.dumps(p.get('themeParamName')) + ')'
    elif operation == 'getThemeColorParameters':
        code = ('fl') + '.getThemeColorParameters()'
    elif operation == 'getThemeFontInfo':
        code = ('fl') + '.getThemeFontInfo(' + json.dumps(p.get('infoType')) + ', ' + json.dumps(p.get('size')) + ')'
    elif operation == 'isFontInstalled':
        code = ('fl') + '.isFontInstalled(' + json.dumps(p.get('fontName')) + ')'
    elif operation == 'openDocument':
        code = ('fl') + '.openDocument(' + json.dumps(p.get('fileURI')) + ')'
    elif operation == 'openScript':
        code = ('fl') + '.openScript(' + json.dumps(p.get('fileURI')) + ')'
    elif operation == 'publishDocument':
        code = ('fl') + '.publishDocument(' + json.dumps(p.get('flaURI')) + ', ' + json.dumps(p.get('publishProfile')) + ')'
    elif operation == 'revertDocument':
        code = ('fl') + '.revertDocument(' + json.dumps(p.get('documentObject')) + ')'
    elif operation == 'saveAll':
        code = ('fl') + '.saveAll()'
    elif operation == 'saveDocument':
        code = ('fl') + '.saveDocument(' + json.dumps(p.get('document')) + ', ' + json.dumps(p.get('fileURI')) + ')'
    elif operation == 'saveDocumentAs':
        code = ('fl') + '.saveDocumentAs(' + json.dumps(p.get('document')) + ')'
    else:
        return json.dumps({"ok": False, "error": "unknown operation: " + operation}, ensure_ascii=False)
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_frame_state(operation: str = "getCustomEase", params: str = "{}") -> str:
    """(jsfl) frame.* state/query commands (merged tool)

    Pick one operation; supply its arguments as a JSON string in `params`.

    Args:
        operation: getCustomEase, getMotionObjectXML, getSoundEnvelope, getSoundEnvelopeLimits, hasMotionPath, is3DMotionObject, isEmpty, isMotionObject
        params: JSON object of the operation's arguments, e.g. '{"fileURI": "file:///C:/x.fla"}'.

    Supported operations:
        - getCustomEase(property)
        - getMotionObjectXML()
        - getSoundEnvelope()
        - getSoundEnvelopeLimits()
        - hasMotionPath()
        - is3DMotionObject()
        - isEmpty()
        - isMotionObject()
    """
    p = json.loads(params) if params else {}
    if operation == 'getCustomEase':
        code = ('fl.getDocumentDOM().getTimeline().layers[' + json.dumps(p.get('l', 0)) + '].frames[' + json.dumps(p.get('f', 0)) + ']') + '.getCustomEase(' + json.dumps(p.get('property')) + ')'
    elif operation == 'getMotionObjectXML':
        code = ('fl.getDocumentDOM().getTimeline().layers[' + json.dumps(p.get('l', 0)) + '].frames[' + json.dumps(p.get('f', 0)) + ']') + '.getMotionObjectXML()'
    elif operation == 'getSoundEnvelope':
        code = ('fl.getDocumentDOM().getTimeline().layers[' + json.dumps(p.get('l', 0)) + '].frames[' + json.dumps(p.get('f', 0)) + ']') + '.getSoundEnvelope()'
    elif operation == 'getSoundEnvelopeLimits':
        code = ('fl.getDocumentDOM().getTimeline().layers[' + json.dumps(p.get('l', 0)) + '].frames[' + json.dumps(p.get('f', 0)) + ']') + '.getSoundEnvelopeLimits()'
    elif operation == 'hasMotionPath':
        code = ('fl.getDocumentDOM().getTimeline().layers[' + json.dumps(p.get('l', 0)) + '].frames[' + json.dumps(p.get('f', 0)) + ']') + '.hasMotionPath()'
    elif operation == 'is3DMotionObject':
        code = ('fl.getDocumentDOM().getTimeline().layers[' + json.dumps(p.get('l', 0)) + '].frames[' + json.dumps(p.get('f', 0)) + ']') + '.is3DMotionObject()'
    elif operation == 'isEmpty':
        code = ('fl.getDocumentDOM().getTimeline().layers[' + json.dumps(p.get('l', 0)) + '].frames[' + json.dumps(p.get('f', 0)) + ']') + '.isEmpty()'
    elif operation == 'isMotionObject':
        code = ('fl.getDocumentDOM().getTimeline().layers[' + json.dumps(p.get('l', 0)) + '].frames[' + json.dumps(p.get('f', 0)) + ']') + '.isMotionObject()'
    else:
        return json.dumps({"ok": False, "error": "unknown operation: " + operation}, ensure_ascii=False)
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_item_state(operation: str = "getData", params: str = "{}") -> str:
    """(jsfl) item.* state/query commands (merged tool)

    Pick one operation; supply its arguments as a JSON string in `params`.

    Args:
        operation: getData, getPublishData, hasData
        params: JSON object of the operation's arguments, e.g. '{"fileURI": "file:///C:/x.fla"}'.

    Supported operations:
        - getData(name)
        - getPublishData(name, format)
        - hasData(name)
    """
    p = json.loads(params) if params else {}
    if operation == 'getData':
        code = ('fl.getDocumentDOM().library.items[' + json.dumps(p.get('i', 0)) + ']') + '.getData(' + json.dumps(p.get('name')) + ')'
    elif operation == 'getPublishData':
        code = ('fl.getDocumentDOM().library.items[' + json.dumps(p.get('i', 0)) + ']') + '.getPublishData(' + json.dumps(p.get('name')) + ', ' + json.dumps(p.get('format')) + ')'
    elif operation == 'hasData':
        code = ('fl.getDocumentDOM().library.items[' + json.dumps(p.get('i', 0)) + ']') + '.hasData(' + json.dumps(p.get('name')) + ')'
    else:
        return json.dumps({"ok": False, "error": "unknown operation: " + operation}, ensure_ascii=False)
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_library_state(operation: str = "findItemIndex", params: str = "{}") -> str:
    """(jsfl) library.* state/query commands (merged tool)

    Pick one operation; supply its arguments as a JSON string in `params`.

    Args:
        operation: findItemIndex, getItemProperty, getItemType, getSelectedItems
        params: JSON object of the operation's arguments, e.g. '{"fileURI": "file:///C:/x.fla"}'.

    Supported operations:
        - findItemIndex(namePath)
        - getItemProperty(property)
        - getItemType(namePath)
        - getSelectedItems()
    """
    p = json.loads(params) if params else {}
    if operation == 'findItemIndex':
        code = ('fl.getDocumentDOM().library') + '.findItemIndex(' + json.dumps(p.get('namePath')) + ')'
    elif operation == 'getItemProperty':
        code = ('fl.getDocumentDOM().library') + '.getItemProperty(' + json.dumps(p.get('property')) + ')'
    elif operation == 'getItemType':
        code = ('fl.getDocumentDOM().library') + '.getItemType(' + json.dumps(p.get('namePath')) + ')'
    elif operation == 'getSelectedItems':
        code = ('fl.getDocumentDOM().library') + '.getSelectedItems()'
    else:
        return json.dumps({"ok": False, "error": "unknown operation: " + operation}, ensure_ascii=False)
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_output_panel_state(operation: str = "save", params: str = "{}") -> str:
    """(jsfl) outputPanel.* state/query commands (merged tool)

    Pick one operation; supply its arguments as a JSON string in `params`.

    Args:
        operation: save
        params: JSON object of the operation's arguments, e.g. '{"fileURI": "file:///C:/x.fla"}'.

    Supported operations:
        - save(fileURI, bAppendToFile, bUseSystemEncoding)
    """
    p = json.loads(params) if params else {}
    if operation == 'save':
        code = ('fl.outputPanel') + '.save(' + json.dumps(p.get('fileURI')) + ', ' + json.dumps(p.get('bAppendToFile')) + ', ' + json.dumps(p.get('bUseSystemEncoding')) + ')'
    else:
        return json.dumps({"ok": False, "error": "unknown operation: " + operation}, ensure_ascii=False)
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_path_state(operation: str = "close", params: str = "{}") -> str:
    """(jsfl) path.* state/query commands (merged tool)

    Pick one operation; supply its arguments as a JSON string in `params`.

    Args:
        operation: close
        params: JSON object of the operation's arguments, e.g. '{"fileURI": "file:///C:/x.fla"}'.

    Supported operations:
        - close()
    """
    p = json.loads(params) if params else {}
    if operation == 'close':
        code = ('fl.drawingLayer.newPath()') + '.close()'
    else:
        return json.dumps({"ok": False, "error": "unknown operation: " + operation}, ensure_ascii=False)
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_shape_state(operation: str = "getCubicSegmentPoints", params: str = "{}") -> str:
    """(jsfl) shape.* state/query commands (merged tool)

    Pick one operation; supply its arguments as a JSON string in `params`.

    Args:
        operation: getCubicSegmentPoints
        params: JSON object of the operation's arguments, e.g. '{"fileURI": "file:///C:/x.fla"}'.

    Supported operations:
        - getCubicSegmentPoints(cubicSegmentIndex)
    """
    p = json.loads(params) if params else {}
    if operation == 'getCubicSegmentPoints':
        code = ('fl.getDocumentDOM().selection[' + json.dumps(p.get('i', 0)) + ']') + '.getCubicSegmentPoints(' + json.dumps(p.get('cubicSegmentIndex')) + ')'
    else:
        return json.dumps({"ok": False, "error": "unknown operation: " + operation}, ensure_ascii=False)
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_text_state(operation: str = "getTextAttr", params: str = "{}") -> str:
    """(jsfl) text.* state/query commands (merged tool)

    Pick one operation; supply its arguments as a JSON string in `params`.

    Args:
        operation: getTextAttr, getTextString
        params: JSON object of the operation's arguments, e.g. '{"fileURI": "file:///C:/x.fla"}'.

    Supported operations:
        - getTextAttr(attrName, startIndex, endIndex)
        - getTextString(startIndex, endIndex)
    """
    p = json.loads(params) if params else {}
    if operation == 'getTextAttr':
        code = ('fl.getDocumentDOM().selection[' + json.dumps(p.get('i', 0)) + ']') + '.getTextAttr(' + json.dumps(p.get('attrName')) + ', ' + json.dumps(p.get('startIndex')) + ', ' + json.dumps(p.get('endIndex')) + ')'
    elif operation == 'getTextString':
        code = ('fl.getDocumentDOM().selection[' + json.dumps(p.get('i', 0)) + ']') + '.getTextString(' + json.dumps(p.get('startIndex')) + ', ' + json.dumps(p.get('endIndex')) + ')'
    else:
        return json.dumps({"ok": False, "error": "unknown operation: " + operation}, ensure_ascii=False)
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_timeline_state(operation: str = "findLayerIndex", params: str = "{}") -> str:
    """(jsfl) timeline.* state/query commands (merged tool)

    Pick one operation; supply its arguments as a JSON string in `params`.

    Args:
        operation: findLayerIndex, getBounds, getFrameProperty, getGuidelines, getLayerProperty, getSelectedFrames, getSelectedLayers, selectAllFrames, setSelectedFrames, setSelectedLayers
        params: JSON object of the operation's arguments, e.g. '{"fileURI": "file:///C:/x.fla"}'.

    Supported operations:
        - findLayerIndex(name)
        - getBounds(frame, includeHiddenLayers)
        - getFrameProperty(property, startframeIndex, endFrameIndex)
        - getGuidelines()
        - getLayerProperty(property)
        - getSelectedFrames()
        - getSelectedLayers()
        - selectAllFrames()
        - setSelectedFrames(startFrameIndex, endFrameIndex, bReplaceCurrentSelection, bReplaceCurrentSelection)
        - setSelectedLayers(index, bReplaceCurrentSelection)
    """
    p = json.loads(params) if params else {}
    if operation == 'findLayerIndex':
        code = ('fl.getDocumentDOM().getTimeline()') + '.findLayerIndex(' + json.dumps(p.get('name')) + ')'
    elif operation == 'getBounds':
        code = ('fl.getDocumentDOM().getTimeline()') + '.getBounds(' + json.dumps(p.get('frame')) + ', ' + json.dumps(p.get('includeHiddenLayers')) + ')'
    elif operation == 'getFrameProperty':
        code = ('fl.getDocumentDOM().getTimeline()') + '.getFrameProperty(' + json.dumps(p.get('property')) + ', ' + json.dumps(p.get('startframeIndex')) + ', ' + json.dumps(p.get('endFrameIndex')) + ')'
    elif operation == 'getGuidelines':
        code = ('fl.getDocumentDOM().getTimeline()') + '.getGuidelines()'
    elif operation == 'getLayerProperty':
        code = ('fl.getDocumentDOM().getTimeline()') + '.getLayerProperty(' + json.dumps(p.get('property')) + ')'
    elif operation == 'getSelectedFrames':
        code = ('fl.getDocumentDOM().getTimeline()') + '.getSelectedFrames()'
    elif operation == 'getSelectedLayers':
        code = ('fl.getDocumentDOM().getTimeline()') + '.getSelectedLayers()'
    elif operation == 'selectAllFrames':
        code = ('fl.getDocumentDOM().getTimeline()') + '.selectAllFrames()'
    elif operation == 'setSelectedFrames':
        code = ('fl.getDocumentDOM().getTimeline()') + '.setSelectedFrames(' + json.dumps(p.get('startFrameIndex')) + ', ' + json.dumps(p.get('endFrameIndex')) + ', ' + json.dumps(p.get('bReplaceCurrentSelection')) + ', ' + json.dumps(p.get('bReplaceCurrentSelection')) + ')'
    elif operation == 'setSelectedLayers':
        code = ('fl.getDocumentDOM().getTimeline()') + '.setSelectedLayers(' + json.dumps(p.get('index')) + ', ' + json.dumps(p.get('bReplaceCurrentSelection')) + ')'
    else:
        return json.dumps({"ok": False, "error": "unknown operation: " + operation}, ensure_ascii=False)
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_tools_state(operation: str = "getKeyDown", params: str = "{}") -> str:
    """(jsfl) tools.* state/query commands (merged tool)

    Pick one operation; supply its arguments as a JSON string in `params`.

    Args:
        operation: getKeyDown
        params: JSON object of the operation's arguments, e.g. '{"fileURI": "file:///C:/x.fla"}'.

    Supported operations:
        - getKeyDown()
    """
    p = json.loads(params) if params else {}
    if operation == 'getKeyDown':
        code = ('fl.tools') + '.getKeyDown()'
    else:
        return json.dumps({"ok": False, "error": "unknown operation: " + operation}, ensure_ascii=False)
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


@mcp.tool()
def jsfl_vertex_state(operation: str = "getHalfEdge", params: str = "{}") -> str:
    """(jsfl) vertex.* state/query commands (merged tool)

    Pick one operation; supply its arguments as a JSON string in `params`.

    Args:
        operation: getHalfEdge
        params: JSON object of the operation's arguments, e.g. '{"fileURI": "file:///C:/x.fla"}'.

    Supported operations:
        - getHalfEdge()
    """
    p = json.loads(params) if params else {}
    if operation == 'getHalfEdge':
        code = ('fl.getDocumentDOM().selection[' + json.dumps(p.get('i', 0)) + '].edges[' + json.dumps(p.get('j', 0)) + '].getHalfEdge(' + json.dumps(p.get('h', 0)) + ').getVertex()') + '.getHalfEdge()'
    else:
        return json.dumps({"ok": False, "error": "unknown operation: " + operation}, ensure_ascii=False)
    result = bridge.submit("run", {"code": code}, timeout=15.0)
    return json.dumps(result, ensure_ascii=False)


if __name__ == "__main__":
    _write_config()
    _clean_startup()
    mcp.run()

