var mcpURI = "file:///C:/Users/hvkmjij/Documents/flash/mcp/";
var outURI = mcpURI + "diag-out.txt";
var report = [];

function trace(t) {
  fl.trace(t);
  report.push(t);
}

function writeReport() {
  FLfile.write(outURI, report.join("\n"), "write");
}

function buildVariant(name, mode) {
  var doc = null;
  try {
    doc = fl.createDocument("timeline");
    var code = "import adobe.utils.MMExecute;\n" +
               "setInterval(function():void { MMExecute('fl.runScript(\"file:///C:/Users/hvkmjij/Documents/flash/mcp/flash-mcp.jsfl\")'); }, 1000);";
    var tl = doc.getTimeline();
    var scriptLayer = 0;
    if (mode === "B") {
      tl.addNewLayer("actions");
      scriptLayer = tl.layerCount - 1;
    }
    tl.layers[scriptLayer].frames[0].actionScript = code;
    var back = tl.layers[scriptLayer].frames[0].actionScript;
    trace("[" + name + "] readback=" + (back === null ? "null" : "len" + back.length + ":" + back.substring(0, 40).replace(/\n/g, " ")));
    doc.width = 240;
    doc.height = 60;
    var saved = false;
    var savePath = "";
    if (mode === "A") {
      try { doc.saveAs(mcpURI + name + ".fla"); savePath = mcpURI + name + ".fla"; } catch (e) { trace("[" + name + "] saveAs URI ERR: " + (e.message || e)); }
    } else if (mode === "B") {
      try { doc.saveAs(mcpURI + name + ".fla"); savePath = mcpURI + name + ".fla"; } catch (e) { trace("[" + name + "] saveAs URI ERR: " + (e.message || e)); }
    } else if (mode === "C") {
      savePath = "none";
    }
    saved = (savePath !== "" && FLfile.exists(savePath));
    trace("[" + name + "] saved=" + saved + " path=" + savePath);
    var ex = doc.exportSWF(mcpURI + name + ".swf", true);
    trace("[" + name + "] export=" + ex);
    try { doc.close(false); } catch (e) { trace("[" + name + "] close ERR"); }
  } catch (e) {
    trace("[" + name + "] EXCEPTION: " + (e.message || e));
  }
}

buildVariant("diag-panel-a", "A");
buildVariant("diag-panel-b", "B");
buildVariant("diag-panel-c", "C");
writeReport();
trace("diag done");
