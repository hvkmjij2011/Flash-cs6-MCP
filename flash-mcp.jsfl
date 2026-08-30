var scriptURI = fl.scriptURI;
var packageURI = scriptURI.substring(0, scriptURI.lastIndexOf("/")) + "/";
var configURI = packageURI + "config.json";

var inboxURI = "";
var outboxURI = "";
var logURI = "";
var screenshotsURI = "";
var logBuffer = [];

function timestamp() {
  var d = new Date();
  function p(n) { return (n < 10 ? "0" : "") + n; }
  return d.getFullYear() + "-" + p(d.getMonth() + 1) + "-" + p(d.getDate()) +
         " " + p(d.getHours()) + ":" + p(d.getMinutes()) + ":" + p(d.getSeconds());
}

function writeLog(level, msg, skipBuffer) {
  var line = timestamp() + " [" + level + "] " + msg;
  fl.trace(line);
  if (logURI) FLfile.write(logURI, line + "\n", "append");
  if (!skipBuffer) {
    logBuffer.push(line);
    if (logBuffer.length > 500) logBuffer.splice(0, logBuffer.length - 500);
  }
}

function loadConfig() {
  var text = FLfile.read(configURI);
  if (!text || text.length === 0) return false;
  try {
    var cfg = eval("(" + text + ")");
    inboxURI = cfg.inbox;
    outboxURI = cfg.outbox;
    logURI = cfg.log;
    screenshotsURI = cfg.screenshots;
    if (inboxURI.charAt(inboxURI.length - 1) !== "/") inboxURI += "/";
    if (outboxURI.charAt(outboxURI.length - 1) !== "/") outboxURI += "/";
    if (screenshotsURI && screenshotsURI.charAt(screenshotsURI.length - 1) !== "/") screenshotsURI += "/";
    FLfile.createFolder(inboxURI);
    FLfile.createFolder(outboxURI);
    if (screenshotsURI) FLfile.createFolder(screenshotsURI);
    var logDir = logURI.substring(0, logURI.lastIndexOf("/"));
    FLfile.createFolder(logDir);
    return true;
  } catch (e) {
    return false;
  }
}

function toJSON(obj) {
  if (obj === null || obj === undefined) return "null";
  var t = typeof obj;
  if (t === "number" || t === "boolean") return String(obj);
  if (t === "string") return '"' + obj.replace(/\\/g, "\\\\").replace(/"/g, '\\"').replace(/\n/g, "\\n") + '"';
  if (t === "function") return "null";
  var out = [], i, key, v;
  if (obj instanceof Array) {
    for (i = 0; i < obj.length; i++) out.push(toJSON(obj[i]));
    return "[" + out.join(",") + "]";
  }
  for (key in obj) {
    if (obj[key] === undefined) continue;
    v = toJSON(obj[key]);
    if (v !== null) out.push('"' + key + '":' + v);
  }
  return "{" + out.join(",") + "}";
}

function getProjectState() {
  var doc = fl.getDocumentDOM();
  if (!doc) return { error: "no open document" };
  var tl = doc.getTimeline();
  var layers = [];
  for (var i = 0; i < tl.layerCount; i++) {
    layers.push({ name: tl.layers[i].name, frames: tl.layers[i].frameCount });
  }
  return {
    name: doc.name,
    width: doc.width,
    height: doc.height,
    frameRate: doc.frameRate,
    currentFrame: tl.currentFrame,
    layers: layers
  };
}

function getFrameDetails(idx) {
  var doc = fl.getDocumentDOM();
  if (!doc) return { error: "no open document" };
  var tl = doc.getTimeline();
  var out = [];
  var maxFrames = 0;
  for (var i = 0; i < tl.layerCount; i++) {
    var L = tl.layers[i];
    var f = L.frames[idx];
    var rec = { layer: L.name, index: i, exists: (f != null), frameCount: L.frameCount };
    if (f) {
      rec.keyframe = (f.frameNumber === idx);
      rec.isBlank = f.isBlank;
      rec.duration = f.duration;
      rec.elementCount = (f.elementCount !== undefined) ? f.elementCount : f.elements.length;
    }
    out.push(rec);
    if (L.frameCount > maxFrames) maxFrames = L.frameCount;
  }
  return { frame: idx, totalFrames: maxFrames, layers: out };
}

function executeCommand(cmdJson) {
  var cmd;
  try { cmd = eval("(" + cmdJson + ")"); }
  catch (e) { return toJSON({ id: null, ok: false, error: "bad command json" }); }
  var id = cmd.id;
  try {
    switch (cmd.type) {
      case "ping":
        return toJSON({ id: id, ok: true, data: "pong" });
      case "run":
        var r = eval(cmd.args.code);
        return toJSON({ id: id, ok: true, data: (r === undefined ? "ok" : String(r)) });
      case "new_project":
        var a = cmd.args;
        var ndoc = fl.createDocument(a.doc_type);
        ndoc.width = a.width;
        ndoc.height = a.height;
        ndoc.frameRate = a.fps;
        if (a.name) {
          var nsaved = fl.saveDocument(ndoc, a.name);
          if (!nsaved) return toJSON({ id: id, ok: false, error: "saveDocument failed for " + a.name });
        }
        return toJSON({ id: id, ok: true, data: getProjectState() });
      case "get_project_state":
        return toJSON({ id: id, ok: true, data: getProjectState() });
      case "read_log":
        var depth = cmd.args.depth || 20;
        var lines = [];
        var content = FLfile.read(logURI);
        if (content) {
          var parts = content.split("\n");
          for (var li = Math.max(0, parts.length - depth - 1); li < parts.length - 1; li++) {
            if (parts[li]) lines.push(parts[li]);
          }
        }
        return toJSON({ id: id, ok: true, data: lines });
      case "frame_details":
        return toJSON({ id: id, ok: true, data: getFrameDetails(cmd.args.frame) });
      case "take_screenshot":
        var sdoc = fl.getDocumentDOM();
        if (!sdoc) return toJSON({ id: id, ok: false, error: "no open document" });
        var d = new Date();
        function pad(n) { return (n < 10 ? "0" : "") + n; }
        var sname = pad(d.getHours()) + "-" + pad(d.getMinutes()) + "-" + pad(d.getSeconds()) +
                    "-" + pad(d.getDate()) + "-" + pad(d.getMonth() + 1) + "-" + d.getFullYear() +
                    "-screendump.png";
        var suri = screenshotsURI + sname;
        var sok = sdoc.exportPNG(suri, true, true);
        return toJSON({ id: id, ok: sok, data: (sok ? suri : "export failed") });
      case "new_keyframe":
        var ktl = fl.getDocumentDOM().getTimeline();
        ktl.setSelectedLayers(cmd.args.layer);
        ktl.currentLayer = cmd.args.layer;
        ktl.insertKeyframe(cmd.args.frame);
        return toJSON({ id: id, ok: true, data: "keyframe at layer " + cmd.args.layer + " frame " + cmd.args.frame });
      case "new_blank_keyframe":
        var btl = fl.getDocumentDOM().getTimeline();
        btl.setSelectedLayers(cmd.args.layer);
        btl.currentLayer = cmd.args.layer;
        btl.insertBlankKeyframe(cmd.args.frame);
        return toJSON({ id: id, ok: true, data: "blank keyframe at layer " + cmd.args.layer + " frame " + cmd.args.frame });
      case "select_frame":
        var ftl = fl.getDocumentDOM().getTimeline();
        ftl.currentFrame = cmd.args.frame;
        return toJSON({ id: id, ok: true, data: "selected frame " + cmd.args.frame });
      case "save_file":
        var sdoc = fl.getDocumentDOM();
        if (!sdoc) return toJSON({ id: id, ok: false, error: "no open document" });
        var spath = cmd.args.path;
        if (spath) {
          var sok = fl.saveDocument(sdoc, spath);
          return toJSON({ id: id, ok: sok, data: (sok ? spath : "saveDocument failed") });
        }
        var sok2 = sdoc.save();
        return toJSON({ id: id, ok: sok2, data: (sok2 ? "saved" : "save() failed") });
      case "clear_scene":
        var cdoc = fl.getDocumentDOM();
        if (!cdoc) return toJSON({ id: id, ok: false, error: "no open document" });
        cdoc.selectAll();
        var cn = cdoc.selection.length;
        cdoc.deleteSelection();
        return toJSON({ id: id, ok: true, data: "cleared " + cn + " selected item(s)" });
      case "move_shape":
        var mdoc = fl.getDocumentDOM();
        if (!mdoc) return toJSON({ id: id, ok: false, error: "no open document" });
        var mtl = mdoc.getTimeline();
        var mli = cmd.args.layer;
        var mfrIdx = (cmd.args.frame !== undefined) ? cmd.args.frame : mtl.currentFrame;
        var mfr = mtl.layers[mli].frames[mfrIdx];
        if (!mfr || !mfr.elements || mfr.elements.length === 0)
          return toJSON({ id: id, ok: false, error: "no element on layer " + mli + " frame " + mfrIdx });
        var mel = mfr.elements[0];
        var mfrom = { x: mel.x, y: mel.y };
        mel.x = cmd.args.x;
        mel.y = cmd.args.y;
        return toJSON({ id: id, ok: true, data: "moved " + mel.elementType + " from x=" + mfrom.x + " y=" + mfrom.y +
                       " to x=" + mel.x + " y=" + mel.y });
      case "one_point_move":
        var opd = fl.getDocumentDOM();
        if (!opd) return toJSON({ id: id, ok: false, error: "no open document" });
        var opt = opd.getTimeline();
        var opl = cmd.args.layer;
        var opf = (cmd.args.frame !== undefined) ? cmd.args.frame : opt.currentFrame;
        if (!opt.layers[opl]) return toJSON({ id: id, ok: false, error: "no layer " + opl });
        var opname = opt.layers[opl].name;
        var oprm = /^rect_#([0-9a-fA-F]{6})_([-0-9.]+),([-0-9.]+)_([-0-9.]+),([-0-9.]+)_([-0-9.]+),([-0-9.]+)_([-0-9.]+),([-0-9.]+)$/.exec(opname);
        if (oprm) {
          var oprp = cmd.args.point;
          if (oprp < 0 || oprp > 3) return toJSON({ id: id, ok: false, error: "point must be 0-3 for a rect (TL, TR, BR, BL)" });
          var oprCorners = [
            [parseFloat(oprm[2]), parseFloat(oprm[3])],
            [parseFloat(oprm[4]), parseFloat(oprm[5])],
            [parseFloat(oprm[6]), parseFloat(oprm[7])],
            [parseFloat(oprm[8]), parseFloat(oprm[9])]
          ];
          var oprpx = oprCorners[oprp][0], oprpy = oprCorners[oprp][1];
          var oprnx = cmd.args.x, oprny = cmd.args.y;
          var oprfrm = opt.layers[opl].frames[opf];
          if (!oprfrm || !oprfrm.elements || oprfrm.elements.length === 0)
            return toJSON({ id: id, ok: false, error: "no element on layer " + opl + " frame " + opf });
          var oprShape = oprfrm.elements[0];
          var oprFound = false;
          var oprErr = "";
          oprShape.beginEdit();
          for (var oprE = 0; oprE < oprShape.edges.length; oprE++) {
            var oprC2 = oprShape.edges[oprE].getControl(2);
            if (Math.abs(oprC2.x - oprpx) + Math.abs(oprC2.y - oprpy) < 0.5) {
              try {
                oprShape.edges[oprE].setControl(2, oprnx, oprny);
                oprFound = true;
              } catch (e2) { oprErr = String(e2.message || e2); }
              break;
            }
          }
          oprShape.endEdit();
          if (!oprFound)
            return toJSON({ id: id, ok: false, error: oprErr || ("corner " + oprpx + "," + oprpy + " not found in shape") });
          oprCorners[oprp] = [oprnx, oprny];
          var oprNewName = "rect_#" + oprm[1] + "_" +
            oprCorners[0][0] + "," + oprCorners[0][1] + "_" +
            oprCorners[1][0] + "," + oprCorners[1][1] + "_" +
            oprCorners[2][0] + "," + oprCorners[2][1] + "_" +
            oprCorners[3][0] + "," + oprCorners[3][1];
          opt.layers[opl].name = oprNewName;
          return toJSON({ id: id, ok: true, data: "moved corner " + oprp + " of rect to (" + oprnx + "," + oprny +
                         "); corners now TL(" + oprCorners[0][0] + "," + oprCorners[0][1] +
                         ") TR(" + oprCorners[1][0] + "," + oprCorners[1][1] +
                         ") BR(" + oprCorners[2][0] + "," + oprCorners[2][1] +
                         ") BL(" + oprCorners[3][0] + "," + oprCorners[3][1] + ")" });
        }
        var opm = /^line_#([0-9a-fA-F]{6})_(\d+)_([-0-9.]+),([-0-9.]+)_([-0-9.]+),([-0-9.]+)$/.exec(opname);
        if (!opm) return toJSON({ id: id, ok: false, error: "layer " + opl + " is not a line or rect layer (name: " + opname + ")" });
        var opcolor = "#" + opm[1], opth = parseFloat(opm[2]);
        var opaX = parseFloat(opm[3]), opaY = parseFloat(opm[4]);
        var opbX = parseFloat(opm[5]), opbY = parseFloat(opm[6]);
        var opnx = cmd.args.x, opny = cmd.args.y;
        var opfx, opfy;
        if (cmd.args.point === 0) { opfx = opbX; opfy = opbY; }
        else { opfx = opaX; opfy = opaY; }
        var opnA, opnB;
        if (cmd.args.point === 0) { opnA = [opnx, opny]; opnB = [opbX, opbY]; }
        else { opnA = [opaX, opaY]; opnB = [opnx, opny]; }
        var opnlen = Math.sqrt((opnA[0] - opnB[0]) * (opnA[0] - opnB[0]) + (opnA[1] - opnB[1]) * (opnA[1] - opnB[1]));
        if (opnlen < 0.01) opnlen = 1;
        var opnang = Math.atan2(opnB[1] - opnA[1], opnB[0] - opnA[0]) * 180 / Math.PI;
        var opmidX = (opnA[0] + opnB[0]) / 2, opmidY = (opnA[1] + opnB[1]) / 2;
        var opNewName = "line_" + opcolor + "_" + opth + "_" + opnA[0] + "," + opnA[1] + "_" + opnB[0] + "," + opnB[1];
        var opfrm = opt.layers[opl].frames[opf];
        if (!opfrm || !opfrm.elements || opfrm.elements.length === 0)
          return toJSON({ id: id, ok: false, error: "no element on layer " + opl + " frame " + opf });
        var opel = opfrm.elements[0];
        opd.selectNone();
        opd.selection = [opel];
        opd.deleteSelection();
        opd.selectNone();
        opt.deleteLayer(opl);
        var opNewIdx = opt.addNewLayer(opNewName);
        if (typeof opNewIdx !== "number") opNewIdx = opt.currentLayer;
        opd.addNewRectangle({ left: 0, top: -opth / 2, right: opnlen, bottom: opth / 2 }, 0);
        opd.selectNone();
        var opels = opt.layers[opNewIdx].frames[0].elements;
        var opsel = [];
        for (var opi = 0; opi < opels.length; opi++) opsel.push(opels[opi]);
        opd.selection = opsel;
        opd.setFillColor(opcolor);
        opd.selectNone();
        var opnew = opt.layers[opNewIdx].frames[0].elements[0];
        opnew.x = opmidX; opnew.y = opmidY; opnew.transformX = opmidX; opnew.transformY = opmidY; opnew.rotation = opnang;
        return toJSON({ id: id, ok: true, data: "moved point " + cmd.args.point + " to (" + opnx + "," + opny +
                       "); line is now (" + opnA[0] + "," + opnA[1] + ") -> (" + opnB[0] + "," + opnB[1] +
                       ") on new layer index " + opNewIdx });
      default:
        return toJSON({ id: id, ok: false, error: "unknown command: " + cmd.type });
    }
  } catch (e) {
    return toJSON({ id: id, ok: false, error: String(e.message || e) });
  }
}

function runOnce() {
  if (!loadConfig()) {
    fl.trace("config.json not found at " + configURI);
    return;
  }
  var files = FLfile.listFolder(inboxURI, "files");
  if (!files || files.length === 0) {
    return;
  }
  var f = files[0];
  var content = FLfile.read(inboxURI + f);
  FLfile.remove(inboxURI + f);
  writeLog("info", "got command [" + f + "]: " + content);
  var result = executeCommand(content);
  var outName = f.replace(/\.json$/i, "") + ".result.json";
  FLfile.write(outboxURI + outName, result, "write");
  writeLog("info", "result written [" + outName + "]: " + result);
}

runOnce();
