fl.trace("flash-mcp panel build starting...");

var mcpURI = "file:///C:/Users/hvkmjij/Documents/flash/mcp/";

var code = "import adobe.utils.MMExecute;\n" +
           "setInterval(function():void { MMExecute('fl.runScript(\"" + mcpURI + "flash-mcp.jsfl\")'); }, 1000);";

var doc = fl.createDocument("timeline");
doc.getTimeline().layers[0].frames[0].actionScript = code;
doc.width = 240;
doc.height = 60;
var saved = false;
try {
  doc.saveAs(mcpURI + "flash-mcp-panel.fla");
  saved = true;
  fl.trace("FLA saved: " + mcpURI + "flash-mcp-panel.fla");
} catch (e) {
  fl.trace("saveAs failed: " + (e.message || e));
}
var exported = false;
try {
  exported = doc.exportSWF(mcpURI + "flash-mcp-panel.swf", true);
  fl.trace("SWF export result: " + exported);
} catch (e) {
  fl.trace("exportSWF failed: " + (e.message || e));
}
if (exported) {
  doc.close(false);
} else {
  fl.trace("export failed - leaving document open for inspection");
}
fl.trace("panel build done");
