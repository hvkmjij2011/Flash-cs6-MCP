"""Submit a .jsfl file straight to the flash-mcp bridge inbox, bypassing the MCP server.

Usage: python runjsfl.py <script.jsfl> [timeout_seconds]

Long-running scripts kill the MCP stdio connection; the bridge itself handles them fine.
Prints the outbox result, then dumps the Flash Output panel tail.
"""
import json, os, sys, time, uuid, pathlib

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

APPDATA = pathlib.Path(os.environ["APPDATA"]) / "flash-mcp"
INBOX, OUTBOX = APPDATA / "inbox", APPDATA / "outbox"
HERE = pathlib.Path(__file__).resolve().parent
OUT_TXT = HERE / "out.txt"

script = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
timeout = float(sys.argv[2]) if len(sys.argv) > 2 else 180.0

cid = "x-" + uuid.uuid4().hex[:8]
(INBOX / f"{cid}.json").write_text(
    json.dumps({"id": cid, "type": "run", "args": {"code": script}}), encoding="utf-8"
)

res = OUTBOX / f"{cid}.result.json"
deadline = time.time() + timeout
result = None
while time.time() < deadline:
    if res.exists():
        try:
            result = json.loads(res.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            time.sleep(0.3); continue
        res.unlink(missing_ok=True)
        break
    time.sleep(0.3)

print("RESULT:", json.dumps(result, ensure_ascii=False) if result else "NO RESULT (script aborted in Flash)")

# dump the Output panel so traces / the real error are visible either way
dump = "d-" + uuid.uuid4().hex[:8]
uri = "file:///" + str(OUT_TXT).replace("\\", "/")
(INBOX / f"{dump}.json").write_text(
    json.dumps({"id": dump, "type": "run",
                "args": {"code": f"fl.outputPanel.save({json.dumps(uri)}, null, null)"}}),
    encoding="utf-8")
time.sleep(3)
(OUTBOX / f"{dump}.result.json").unlink(missing_ok=True)

if OUT_TXT.exists():
    lines = [l for l in OUT_TXT.read_text(encoding="utf-8", errors="replace").splitlines()
             if '"code"' not in l and "outputPanel.save" not in l]
    print("--- output panel tail ---")
    for l in lines[-8:]:
        print(l[:400])
