
## toolObj  (12)

### `toolObj.depth`
an integer that specifies the depth of the tool in the pop-up menu in the Tools panel. This property is used only when creating extensible tools.

### `toolObj.enablePIControl(control, bEnable)`
enables or disables the specified control in a Property inspector. Used only when creating extensible tools.
- **params:** control A string that specifies the name of the control to enable or disable. Legal values depend on the Property inspector invoked by this tool; see toolObj.setPI(). A shape Property inspector has the following controls: A text Property inspector has the following controls: stroke fill type font pointsize color bold italic direction alignLeft alignCenter alignRight alignJustify spacing position autoKern small rotation format lineType selectab...

### `toolObj.iconID`
an integer with a value of -1. This property is used only when you create extensible tools. An iconID value of -1 means that Flash will not try find an icon for the tool. Instead, the script for the tool should specify the icon to display in the Tools panel; see toolObj.setIcon().

### `toolObj.position size publish background framerate player profile`
an integer that specifies the position of the tool in the Tools panel. This property is used only when you create extensible tools.

### `toolObj.setIcon(file)`
identifies a PNG file to use as a tool icon in the Tools panel. This method is used only when you create extensible tools.
- **params:** file A string that specifies the name of the PNG file to use as the icon. The PNG file must be placed in the same folder as the JSFL file.

### `toolObj.setMenuString(menuStr)`
sets the string that appears in the pop-up menu as the name for the tool. This method is used only when you create extensible tools.
- **params:** menuStr A string that specifies the name that appears in the pop-up menu as the name for the tool.

### `toolObj.setOptionsFile(xmlFile)`
associates an XML file with the tool. The file specifies the options to appear in a modal panel that is invoked by an Options button in the Property inspector. You would usually use this method in the configureTool() function inside your JSFL file. See configureTool(). For example, the PolyStar.x...
- **params:** xmlFile A string that specifies the name of the XML file that has the description of the tool’s options. The XML file must be placed in the same folder as the JSFL file.

### `toolObj.setPI(pi)`
specifies which Property inspector should be used when the tool is activated. This method is used only when you create extensible tools. Acceptable values are "shape" (the default), "text", and "movie".
- **params:** pi A string that specifies the Property inspector to invoke for this tool.

### `toolObj.setToolName(name)`
assigns a name to the tool for the configuration of the Tools panel. This method is used only when you create extensible tools. The name is used only by the XML layout file that Flash reads to construct the Tools panel. The name does not appear in the Flash user interface.
- **params:** name A string that specifies the name of the tool.

### `toolObj.setToolTip(toolTip)`
sets the tooltip that appears when the mouse is held over the tool icon. This method is used only when you create extensible tools.
- **params:** toolTip A string that specifies the tooltip to use for the tool.

### `toolObj.showPIControl(control, bShow)`
shows or hides a control in the Property inspector. This method is used only when you create extensible tools.
- **params:** control A string that specifies the name of the control to show or hide. This method is used only when you create extensible tools. Valid values depend on the Property inspector invoked by this tool (see toolObj.setPI()). A shape Property inspector has the following controls: A text Property inspector has the following controls: The movie Property inspector has the following controls: stroke fill type font pointsize color bold italic direction...

### `toolObj.showTransformHandles(bShow)`
called in the configureTool() method of an extensible tool’s JavaScript file to indicate that the free transform handles should appear when the tool is active. This method is used only when you create extensible tools.
- **params:** bShow A Boolean value that determines whether to show or hide the free transform handles for the current tool (true shows the handles; false hides them).

