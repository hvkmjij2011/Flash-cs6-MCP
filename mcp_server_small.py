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




if __name__ == "__main__":
    _write_config()
    _clean_startup()
    mcp.run()

