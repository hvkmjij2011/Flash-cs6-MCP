
## fl  (79)

### `fl.Math`
the Math object provides methods for matrix and point operations.

### `fl.actionsPanel`
an actionsPanel object, which represents the currently displayed Actions panel. For information on using this property, see actionsPanel object.

### `fl.addEventListener(eventType, callbackFunction)`
registers a function to be called when a specific event occurs. Note that you can define multiple listeners for the same event. When using this method, be aware that if the event occurs frequently (as might be the case with mouseMove) and the function takes a long time to run, your application mi...
- **params:** eventType A string that specifies the event type to pass to this callback function. Acceptable values are "documentNew", "documentOpened", "documentClosed", "mouseMove", "documentChanged", "layerChanged""timelineChanged", "frameChanged", “prePublish”, “postPublish”, “selectionChanged”, and dpiChanged. fl.publishCacheMemorySizeMax An integer that sets the memory cache size limit preference. fl.objectDrawingMode An integer that represents the ob...
- **returns:** An integer that identifies the event listener. Use this identifier when calling fl.removeEventListener().

### `fl.as3PackagePaths`
a string that corresponds to the global Classpath setting in the ActionScript 3.0 Settings dialog box. Items in the string are delimited by semi-colons. To view or change ActionScript 2.0 Classpath settings, use fl.packagePaths - dropped.

### `fl.browseForFileURL(browseType [, title [, fileDescription [, fileFilter]]])`
opens a File Open or File Save system dialog box and lets the user specify a file to be opened or saved.
- **params:** browseType A string that specifies the type of file browse operation. Valid values are "open", "select" or "save". The values "open" and "select" open the system File Open dialog box. Each value is provided for compatibility with Dreamweaver. The value "save" opens a system File Save dialog box. title An optional string that specifies the title for the File Open or File Save dialog box. If this parameter is omitted, a default value is used. Th...
- **returns:** The URL of the file, expressed as a file:/// URI; returns null if the user cancels out of the dialog box.

### `fl.browseForFolderURL([description])`
displays a Browse for Folder dialog box and lets the user select a folder.
- **params:** description An optional string that specifies the description of the Browse For Folder dialog box. If this parameter is omitted, the dialog box title is “Select Folder.”
- **returns:** The URL of the folder, expressed as a file:/// URI; returns null if the user cancels out of the dialog box.

### `fl.clearPublishCache()`
empties the publish cache.
- **params:** None.

### `fl.clipCopyString(string)`
copies the specified string to the Clipboard. To copy the current selection to the Clipboard, use document.clipCopy().
- **params:** string A string to be copied to the Clipboard.

### `fl.closeAll([bPromptToSave])`
closes all open files (FLA files, SWF files, JSFL files, and so on). If you want to close all open files without saving changes to any of them, pass false for bPromptToSave. This method does not terminate the application.
- **params:** bPromptToSave An optional Boolean value that specifies whether to display the Save dialog box for any files that have been changed since they were previously saved, or the Save As dialog box for files that have never been saved. The default value is true.

### `fl.closeAllPlayerDocuments()`
closes all the SWF files that were opened with Control > Test Movie.
- **params:** None.
- **returns:** A Boolean value: true if one or more movie windows were open; false otherwise.

### `fl.closeDocument(documentObject [, bPromptToSaveChanges])`
closes the specified document.
- **params:** documentObject A Document object. If documentObject refers to the active document, the Document window might not close until the script that calls this method finishes executing. bPromptToSaveChanges A Boolean value. When bPromptToSaveChanges is false, the user is not prompted if the document contains unsaved changes; that is, the file is closed and the changes are discarded. If bPromptToSaveChanges is true, and if the document contains unsave...

### `fl.compilerErrors`
a compilerErrors object, which represents the Errors panel. For information on using this property, see compilerErrors object.

### `fl.componentsPanel`
a componentsPanel object, which represents the Components panel.

### `fl.configDirectory`
a string that specifies the full path for the local user’s Configuration directory in a platform- specific format. To specify this path as a file:/// URI, which is not platform-specific, use fl.configURI.

### `fl.configURI`
a string that specifies the full path for the local user’s Configuration directory as a file:/// URI. See also fl.configDirectory.

### `fl.contactSensitiveSelection`
A Boolean value that specifies whether Contact Sensitive selection mode is enabled (true) or not (false).

### `fl.copyLibraryItem(fileURI, libraryItemPath)`
silently copies a library item from a document without exposing the item in the Flash Pro user interface. Call the document.clipPaste() method to paste the item into the new document.
- **params:** fileURI A string, expressed as a file:/// URI, that contains the path to the FLA or XFL file. libraryItemPath A string, that specifies the path to the library item to be copied.
- **returns:** A Boolean value: true if the copy succeeds; false otherwise.

### `fl.createDocument([docType])`
opens a new document and selects it. Values for size, resolution, and color are the same as the current defaults.
- **params:** docType A string that specifies the type of document to create. The only acceptable value is "timeline". The default value is "timeline", which has the same effect as choosing File > New > Flash File (ActionScript 3.0). This parameter is optional.
- **returns:** The Document object for the newly created document, if the method is successful. If an error occurs, the value is undefined.

### `fl.createNewDocList`
an array of strings that represent the various types of documents that can be created.

### `fl.createNewDocListType`
an array of strings that represent the file extensions of the types of documents that can be created. The entries in the array correspond directly (by index) to the entries in the fl.createNewDocList array.

### `fl.createNewTemplateList`
an array of strings that represent the various types of templates that can be created.

### `fl.documents`
an array of Document objects (see Document object) that represent the documents (FLA files) that are currently open for editing.

### `fl.drawingLayer`
the drawingLayer object that an extensible tool should use when the user wants to temporarily draw while dragging (for example, when creating a selection marquee).

### `fl.exportPublishProfileString( ucfURI [, profileName] )`
Returns a specific document’s publishing profile without having to open the file. The publish profile can also be specified, but this is optional.
- **params:** ucfURI A string that specifies the file Uniform Resource Identifier (URI) from which to export the publish settings. profileName A string that specifies the profile name to export. This parameter is optional.
- **returns:** String.

### `fl.externalLibraryPath`
a string that contains a list of items in the global ActionScript 3.0 External library path, which specifies the location of SWC files used as runtime shared libraries. Items in the string are delimited by semi-colons. In the authoring tool, the items are specified by choosing Edit > Preferences ...

### `fl.fileExists(fileURI)`
checks whether a file already exists on disk.
- **params:** fileURI A string, expressed as a file:/// URI, that contains the path to the file.
- **returns:** A Boolean value: true if the file exists on disk; false otherwise.

### `fl.findDocumentDOM(id)`
lets you target a specific file by using its unique identifier (instead of its index value, for example). Use this method in conjunction with document.id.
- **params:** id An integer that represents a unique identifier for a document.
- **returns:** A Document object, or null if no document exists with the specified id.

### `fl.findDocumentIndex(name)`
returns an array of integers that represent the position of the document name in the fl.documents array. More than one document with the same name can be open (if the documents are located in different folders).
- **params:** name The document name for which you want to find the index. The document must be open.
- **returns:** An array of integers that represent the position of the document name in the fl.documents array.

### `fl.findObjectInDocByName(instanceName, document)`
exposes elements in a document with instance names that match the specified text. Note: In some cases, this method works only when run as a command from within a FLA file, not when you are currently viewing or editing the JSFL file.
- **params:** instanceName A string that specifies the instance name of an item in the specified document. document The Document object in which to search for the specified item.
- **returns:** An array of generic objects. Use the .obj property of each item in the array to get the object. The object has the following properties: keyframe, layer, tim...

### `fl.findObjectInDocByType(elementType, document)`
exposes elements of a specified element type in a document. Note: In some cases, this method works only when run as a command from within a FLA file, not when you are currently viewing or editing the JSFL file.
- **params:** elementType A string that represents the type of element to search for. For acceptable values, see element.elementType. document The Document object in which to search for the specified item.
- **returns:** An array of generic objects. Use the .obj property of each item in the array to get the element object. Each object has the following properties: keyframe, l...

### `fl.flexSDKPath`
a string that specifies the path to the Flex SDK folder, which contains bin, frameworks, lib, and other folders. In the authoring tool, the items are specified by choosing Edit > Preferences > ActionScript > ActionScript 3.0 Settings.

### `fl.getAppMemoryInfo(memType)`
Method (Windows only); returns an integer that represents the number of bytes being used in a specified area of Flash.exe memory. Use the following table to determine which value you want to pass as memType: memType Resource data 0 PAGEFAULTCOUNT 1 PEAKWORKINGSETSIZE 2 WORKINGSETSIZE
- **params:** memType An integer that specifies the memory utilization area to be queried. For a list of acceptable values, see the following description.
- **returns:** An integer that represents the number of bytes being used in a specified area of Flash.exe memory.

### `fl.getDocumentDOM()`
retrieves the DOM (Document object) of the currently active document (FLA file). If one or more documents are open but a document does not currently have focus (for example, if a JSFL file has focus), retrieves the DOM of the most recently active document.
- **params:** None.
- **returns:** A Document object, or null if no documents are open.

### `fl.getSwfPanel(panelName, [useLocalizedPanelName])`
returns the SWFPanel object based on the panel's localized name or its SWF filename (without the filename extension).
- **params:** panelName The localized panel name or the root filename of the panel's SWF file. Pass in false as the second parameter if using the latter. useLocalizedPanelName Optional. Defaults to true. If false, the panelName parameter is assumed to be the English (unlocalized) name of the panel, which corresponds to the SWF filename without the file extension.
- **returns:** SWFPanel object.

### `fl.getThemeColor(themeParamName)`
returns the theme color that matches the passed theme parameter. Flash Professional CC introduced 2 UI themes: Dark and Light UI, and this method retrieves the current theme color to help you render your custom content.
- **params:** themeParamName A string that contains a theme parameter from the list returned by the fl.getThemeColorParameters() method. If the theme parameter is themeUseGradients, this method returns either "true" or "false".
- **returns:** A String containing a theme color (in #rrggbb or #rrggbbaa format) that matches the passed parameter. If the theme parameter is themeUseGradients, this metho...

### `fl.getThemeColorParameters()`
returns an Array of strings that contain the theme color parameters. The available theme color parameters are as follows:  themeAppBackgroundColor  themeItemSelectedColor  themeItemHighlightedColor  themeHotTextNormalColor  themeHotTextRolloverColor  themeHotTextDisableColor  themeStaticTe...
- **params:** None.
- **returns:** An Array of strings that contain the theme color parameters.

### `fl.getThemeFontInfo(infoType, size)`
returns either the font Style or the font Size that is used to draw the UI of the specified size.
- **params:** infoType A string that contains one of the following:  fontStyle - Return the font style for the size specified by the size parameter.  fontSize - Return the font size for the size specified by the size parameter. size A string that specifies either "large" or "small".
- **returns:** A String containing either the font style or the font size for the specifie size.

### `fl.installedPlayers()`
The array of generic objects corresponding to the list of installed Flash Players in the document PI. Each object in the array contains the following properties: name The string name of the document. version Can be used to set the current player for a document, using the Document.setPlayerVersion...
- **params:** None.
- **returns:** An array of generic objects corresponding to the list of installed Flash Players in the document PI.

### `fl.isFontInstalled(fontName)`
determines whether a specified font is installed.
- **params:** fontName A string that specifies the name of a device font.
- **returns:** A Boolean value of true if the specified font is installed; false otherwise.

### `fl.languageCode`
a string that returns the five character code identifying the locale of the application’s user interface.

### `fl.libraryPath`
a string that contains a list of items in the global ActionScript 3.0 Library path, which specifies the location of SWC files or folders containing SWC files. Items in the string are delimited by semi-colons. In the authoring tool, the items are specified by choosing Edit > Preferences > ActionSc...

### `fl.mapPlayerURL(URI [, returnMBCS])`
maps an escaped Unicode URL to a UTF-8 or MBCS URL. Use this method when the string will be used in ActionScript to access an external resource. You must use this method if you need to handle multibyte characters.
- **params:** URI A string that contains the escaped Unicode URL to map. returnMBCS A Boolean value that you must set to true if you want an escaped MBCS path returned. Otherwise, the method returns UTF-8. The default value is false. This parameter is optional.
- **returns:** A string that is the converted URL.

### `fl.mruRecentFileList`
an array of the complete filenames in the Most Recently Used (MRU) list that the Flash authoring tool manages.

### `fl.mruRecentFileListType`
an array of the file types in the MRU list that the Flash authoring tool manages. This array corresponds to the array in the fl.mruRecentFileList property.

### `fl.objectDrawingMode`
a Boolean value that specifies whether the object drawing mode is enabled (true) or the merge drawing mode is enabled (false).

### `fl.openDocument(fileURI)`
opens a Flash document (FLA file) for editing in a new Flash Document window and gives it focus. For a user, the effect is the same as selecting File > Open and then selecting a file. If the specified file is already open, the window that contains the document comes to the front. The window that ...
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the name of the file to be opened.
- **returns:** The Document object for the newly opened document, if the method is successful. If the file is not found or is not a valid FLA file, an error is reported and...

### `fl.openScript(fileURI )`
opens an existing file or creates a new script (JSFL, AS, ASC) or other file (XML, TXT) in Flash.
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the path of the JSFL, AS, ASC, XML, TXT, or other file that should be loaded into Flash.

### `fl.outputPanel`
reference to the outputPanel object.

### `fl.presetPanel`
Read-only property: a presetPanel object.

### `fl.publishCacheDiskSizeMax`
Property: an integer that sets the maximum size, in megabytes, of the publish cache on disk.

### `fl.publishCacheEnabled`
Property: a boolean value that sets whether the publish cache is enabled.

### `fl.publishCacheMemoryEntrySizeLimit`
Property: an integer that sets the maximum size, in kilobytes, of entries that can be added to the publish cache in memory. Anything at or below this size will be kept in memory; anything larger will be written to disk. Users with a lot of memory might want to raise this value to increase perform...

### `fl.publishCacheMemorySizeMax`
Property: an integer that sets the maximum size, in megabytes, of the publish cache in memory.

### `fl.publishDocument( flaURI [, publishProfile] )`
publishes a FLA file without opening it. This API opens the FLA in a headless mode and publishes the SWF (or whatever the profile is set to). The second parameter (publishProfile) is optional. The return value is a boolean indicating if the profile was found or not. In the case where the second p...
- **params:** flaURI A string, expressed as a file:/// URI, that specifies the path of the FLA file that should be silently published. publishProfile A string that specifies the publish profile to use when publishing. If this parameter is omitted, the default publish profile is used.
- **returns:** Boolean

### `fl.quit([bPromptIfNeeded])`
quits Flash, prompting the user to save any changed documents.
- **params:** bPromptIfNeeded A Boolean value that is true (default) if you want the user to be prompted to save any modified documents. Set this parameter to false if you do not want the user to be prompted to save modified documents. In the latter case, any modifications in open documents will be discarded and the application will exit immediately. Although it is useful for batch processing, use this method with caution. This parameter is optional.

### `fl.reloadTools()`
rebuilds the Tools panel from the toolconfig.xml file. This method is used only when creating extensible tools. Use this method when you need to reload the Tools panel, for example, after modifying the JSFL file that defines a tool that is already present in the panel.
- **params:** None.

### `fl.removeEventListener(eventType, id)`
Unregisters a function that was registered using fl.addEventListener().
- **params:** eventType A string that specifies the event type to remove from this callback function. Acceptable values are "documentNew", "documentOpened", "documentClosed", "mouseMove", "documentChanged", "layerChanged", "timelineChanged", and "frameChanged". id An integer that specifies the listener ID returned from the corresponding fl.addEventListener() call.
- **returns:** A Boolean value of true if the event listener was successfully removed; false if the function was never added to the list with the fl.addEventListener() method.

### `fl.resetAS3PackagePaths()`
resets the global Classpath setting in the ActionScript 3.0 Settings dialog box to the default value. To reset the ActionScript 2.0 global Classpath, use fl.resetPackagePaths() - dropped.
- **params:** None.

### `fl.revertDocument(documentObject)`
reverts the specified FLA document to its last saved version. Unlike the File > Revert menu option, this method does not display a warning window that asks the user to confirm the operation. See also document.revert() and document.canRevert().
- **params:** documentObject A Document object. If documentObject refers to the active document, the Document window might not revert until the script that calls this method finishes executing.
- **returns:** A Boolean value: true if the Revert operation completes successfully; false otherwise.

### `fl.runScript(fileURI [, funcName [, arg1, arg2, ...]])`
executes a JavaScript file. If a function is specified as one of the arguments, it runs the function and also any code in the script that is not within the function. The rest of the code in the script runs before the function is run.
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the name of the script file to execute. funcName A string that identifies a function to execute in the JSFL file that is specified in fileURI. This parameter is optional. arg An optional parameter that specifies one or more arguments to be passed to funcname.
- **returns:** The function's result as a string, if funcName is specified; otherwise, nothing.

### `fl.saveAll()`
saves all open documents. If a file has never been saved, the Save As dialog box displays. If a file has not been modified since the last time it was saved, the file isn’t saved. To allow an unsaved or unmodified file to be saved, use fl.saveDocumentAs().
- **params:** None.

### `fl.saveDocument(document [, fileURI])`
saves the specified document as a FLA document.
- **params:** document A Document object that specifies the document to be saved. If document is null, the active document is saved. fileURI A string, expressed as a file:/// URI, that specifies the name of the saved document. If the fileURI parameter is null or omitted, the document is saved with its current name. This parameter is optional.
- **returns:** A Boolean value: true if the save operation completes successfully; false otherwise. This method save the file regardless of whether it is new, modified, or ...

### `fl.saveDocumentAs(document)`
displays the Save As dialog box for the specified document.
- **params:** document A Document object that specifies the document to save. If document is null, the active document is saved.
- **returns:** A Boolean value: true if the Save As operation completes successfully; false otherwise.

### `fl.scriptURI`
a string that represents the path of the currently running JSFL script, expressed as a file:/// URI. If the script was called from fl.runScript(), this property represents the path of the immediate parent script. That is, it doesn’t traverse multiple calls to fl.runScript() to find the path of th...

### `fl.selectElement(elementObject, editMode)`
enables selection or editing of an element. Generally, you will use this method on objects returned by fl.findObjectInDocByName() or fl.findObjectInDocByType().
- **params:** elementObject The Element object you want to select. editMode A Boolean value that specifies whether you want to edit the element (true) or want only to select it (false).
- **returns:** A Boolean value of true if the element was successfully selected; false otherwise.

### `fl.selectTool(toolName)`
selects the specified tool in the Tools panel. The acceptable default values for toolName are "arrow", "bezierSelect", "freeXform", "fillXform", "lasso", "pen", "penplus", "penminus", "penmodify", "text", "line", "rect", "oval", "rectPrimitive", "ovalPrimitive", "polystar", "pencil", "brush", "in...
- **params:** toolName A string that specifies the name of the tool to select. See “Description” below for information on acceptable values for this parameter.

### `fl.setActiveWindow(document [, bActivateFrame])`
sets the active window to be the specified document. This method is also supported by Dreamweaver and Fireworks. If the document has multiple views (created by Window > Duplicate Window), the most recently active view is selected.
- **params:** document A Document object that specifies the document to select as the active window. bActivateFrame An optional parameter that is ignored by Flash and Fireworks and is present only for compatibility with Dreamweaver.

### `fl.setPrefBoolean(keySection, keyName, keyValue)`
sets a boolean preference value.
- **params:** keySection A string that contains the preferences section that contains keyName. (usually this is "Settings"). keyName A string that contains the name of the boolean preference setting to be set. keyValue A string that contains the value to be set (true ohr false).
- **returns:** None.

### `fl.showIdleMessage(show)`
lets you disable the warning about a script running too long (pass false for show). You might want to do this when processing batch operations that take a long time to complete. To re-enable the alert, issue the command again, this time passing true for show.
- **params:** show A Boolean value specifying whether to enable or disable the warning about a script running too long.

### `fl.sourcePath`
a string that contains a list of items in the global ActionScript 3.0 Source path, which specifies the location of ActionScript class files. Items in the string are delimited by semi-colons. In the authoring tool, the items are specified by choosing Edit > Preferences > ActionScript > ActionScrip...

### `fl.spriteSheetExporter`
returns an instance of the SpriteSheetExporter object.

### `fl.swfPanels`
an array of registered swfPanel objects (see swfPanel object). A swfPanel object is registered if it has been opened at least once. A panel’s position in the array represents the order in which it was opened. If the first panel opened is named TraceBitmap and the second panel opened is named Anot...

### `fl.toggleBreakpoint(String fileURI, int line, Boolean enable)`
Toggles a breakpoint for the given .as file at the given line. If enable is false, the breakpoint currently stored at that line will be erased.
- **params:** fileURI A string; the URI of the the AS file in which to toggle the breakpoint. line An integer; the line number at which to toggle the breakpoint. enable Boolean; if set to true, the breakpoint is enabled. If set to false, the breakpoint is disabled.

### `fl.tools`
an array of Tools objects (see Tools object). This property is used only when creating extensible tools.

### `fl.trace(message)`
sends a text string to the Output panel, terminated by a new line, and displays the Output panel if it is not already visible. This method is identical to outputPanel.trace() and works in the same way as the trace() statement in ActionScript. To send a blank line, use fl.trace("") or fl.trace("\n...
- **params:** message A string that appears in the Output panel.

### `fl.version`
the long string version of the Flash authoring tool, including platform.

### `fl.xmlPanel(xmlURI)`
Launches the XML To UI dialog from a URI that points to an XML-format file.
- **params:** xmlURI A URI specifying the XML file that defines the controls in the panel. You must specify the full path name.
- **returns:** XMLUI. The object returned contains properties for all controls defined in the XML file. All properties are returned as strings. The returned object will hav...

### `fl.xmlPanelFromString(xmlString)`
Launches the XML To UI dialog from an XML-format string.
- **params:** xmlString A string containing XML that defines a dialog.
- **returns:** XMLUI.

### `fl.xmlui`
an XMLUI object. This property lets you get and set XMLUI properties in a XMLUI dialog box and lets you accept or cancel the dialog box programmatically.

