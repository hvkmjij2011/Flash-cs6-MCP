
## document  (183)

### `document.accName`
a string that is equivalent to the Name field in the Accessibility panel. Screen readers identify objects by reading the name aloud.

### `document.addDataToDocument(name, type, data)`
stores specified data with a document. Data is written to the FLA file and is available to JavaScript when the file reopens.
- **params:** name A string that specifies the name of the data to add. type A string that defines the type of data to add. Acceptable values are "integer", "integerArray", "double", "doubleArray", "string", and "byteArray". data The value to add. Valid types depend on the type parameter.

### `document.addDataToSelection(name, type, data)`
stores specified data with the selected objects. Data is written to the FLA file and is available to JavaScript when the file reopens. Only symbols and bitmaps support persistent data.
- **params:** name A string that specifies the name of the persistent data. type Defines the type of data. Acceptable values are "integer", "integerArray", "double", "doubleArray", "string", and "byteArray". data The value to add. Valid types depend on the type parameter.

### `document.addFilter(filterName)`
applies a filter to the selected objects and places the filter at the end of the Filters list.
- **params:** filterName A string specifying the filter to be added to the Filters list and enabled for the selected objects. Acceptable values are "adjustColorFilter", "bevelFilter", "blurFilter", "dropShadowFilter", "glowFilter", "gradientBevelFilter", and "gradientGlowFilter".

### `document.addItem(position, item)`
adds an item from any open document or library to the specified Document object.
- **params:** position A point that specifies the x and y coordinates of the location at which to add the item. It uses the center of a symbol or the upper left corner of a bitmap or video. item An Item object that specifies the item to add and the library from which to add it (see Item object).
- **returns:** A Boolean value: true if successful; false otherwise.

### `document.addNewLine(startPoint, endpoint)`
adds a new path between two points. The method uses the document’s current stroke attributes and adds the path on the current frame and current layer. This method works in the same way as clicking on the line tool and drawing a line.
- **params:** startpoint A pair of floating-point numbers that specify the x and y coordinates where the line starts. endpoint A pair of floating-point numbers that specify the x and y coordinates where the line ends.

### `document.addNewOval(boundingRectangle [, bSuppressFill [, bSuppressStroke ]])`
adds a new Oval object in the specified bounding rectangle. This method performs the same operation as the Oval tool. The method uses the document’s current default stroke and fill attributes and adds the oval on the current frame and layer. If both bSuppressFill and bSuppressStroke are set to tr...
- **params:** boundingRectangle A rectangle that specifies the bounds of the oval to be added. For information on the format of boundingRectangle, see document.addNewRectangle(). bSuppressFill A Boolean value that, if set to true, causes the method to create the shape without a fill. The default value is false. This parameter is optional. bSuppressStroke A Boolean value that, if set to true, causes the method to create the shape without a stroke. The defaul...

### `document.addNewPrimitiveOval( boundingRectangle [, bSpupressFill [, bSuppressStroke ]] ))`
adds a new oval primitive fitting into the specified bounds. This method performs the same operation as the Oval Primitive tool. The oval primitive uses the document's current default stroke and fill attributes and is added on the current frame and layer. If both bSuppressFill and bSuppressStroke...
- **params:** boundingRectangle A rectangle that specifies the bounds within which the new oval primitive is added. For information on the format of boundingRectangle, see document.addNewRectangle(). bSuppressFill A Boolean value that, if set to true, causes the method to create the oval without a fill. The default value is false. This parameter is optional. bSuppressStroke A Boolean value that, if set to true, causes the method to create the oval without a...

### `document.addNewPrimitiveRectangle( boundingRectangle, roundness, [, bSuppressFill [, bSuppressStroke ]] ))`
adds a new rectangle primitive fitting into the specified bounds. This method performs the same operation as the Rectangle Primitive tool. The rectangle primitive uses the document's current default stroke and fill attributes and is added on the current frame and layer. If both bSuppressFill and ...
- **params:** rect A rectangle that specifies the bounds within which the new rectangle primitive is added. For information on the format of boundingRectangle, see document.addNewRectangle(). roundness An integer between 0 and 999 that represents the number of points used to specify how much the corners should be rounded. bSuppressFill A Boolean value that, if set to true, causes the method to create the rectangle without a fill. The default value is false....

### `document.addNewPublishProfile([profileName])`
adds a new publish profile and makes it the current one.
- **params:** profileName The unique name of the new profile. If you do not specify a name, a default name is provided. This parameter is optional.
- **returns:** An integer that is the index of the new profile in the profiles list. Returns -1 if a new profile cannot be created.

### `document.addNewRectangle(boundingRectangle, roundness [, bSuppressFill [, bSuppressStroke]])`
adds a new rectangle or rounded rectangle, fitting it into the specified bounds. This method performs the same operation as the Rectangle tool. The method uses the document’s current default stroke and fill attributes and adds the rectangle on the current frame and layer. If both bSuppressFill an...
- **params:** boundingRectangle A rectangle that specifies the bounds within which the new rectangle is added, in the format {left:value1,top:value2,right:value3,bottom:value4}. The left and top values specify the location of the upper left corner (e.g., left:0,top:0 represents the upper left corner of the Stage) and the right and bottom values specify the location of the lower-right corner. Therefore, the width of the rectangle is the difference in value b...

### `document.addNewScene([name])`
adds a new scene (Timeline object) as the next scene after the currently selected scene and makes the new scene the currently selected scene. If the specified scene name already exists, the scene is not added and the method returns an error.
- **params:** name Specifies the name of the scene. If you do not specify a name, a new scene name is generated.
- **returns:** A Boolean value: true if the scene is added successfully; false otherwise.

### `document.addNewText(boundingRectangle [, text ])`
inserts a new text field and optionally places text into the field. If you omit the text parameter, you can call document.setTextString() to populate the text field.
- **params:** boundingRectangle Specifies the size and location of the text field. For information on the format of boundingRectangle, see document.addNewRectangle(). text An optional string that specifies the text to place in the field. If you omit this parameter, the selection in the Tools panel switches to the Text tool. Therefore, if you don’t want the selected tool to change, pass a value for text.

### `document.align(alignmode [, bUseDocumentBounds])`
aligns the selection.
- **params:** alignmode A string that specifies how to align the selection. Acceptable values are "left", "right", "top", "bottom", "vertical center", and "horizontal center". bUseDocumentBounds A Boolean value that, if set to true, causes the method to align to the bounds of the document. Otherwise, the method uses the bounds of the selected objects. The default is false. This parameter is optional.

### `document.arrange(arrangeMode)`
arranges the selection on the Stage. This method applies only to non-shape objects.
- **params:** arrangeMode Specifies the direction in which to move the selection. Acceptable values are "back", "backward", "forward", and "front". It provides the same capabilities as these options provide on the Modify > Arrange menu.

### `document.as3AutoDeclare`
a Boolean value that describes whether the instances placed on the Stage are automatically added to user- defined timeline classes. The default value is true.

### `document.as3Dialect`
a string that describes the ActionScript 3.0 “dialect” being used in the specified document. The default value is "AS3". If you wish to allow prototype classes, as permitted in earlier ECMAScript specifications, set this value to "ES".

### `document.as3ExportFrame`
an integer that specifies in which frame to export ActionScript 3.0 classes. By default, classes are exported in Frame 1.

### `document.as3StrictMode`
a Boolean value that specifies whether the ActionScript 3.0 compiler should compile with the Strict Mode option turned on (true) or off (false). Strict Mode causes warnings to be reported as errors, which means that compilation will not succeed if those errors exist. The default value is true.

### `document.as3WarningsMode`
a Boolean value that specifies whether the ActionScript 3.0 compiler should compile with the Warnings Mode option turned on (true) or off (false). Warnings Mode causes extra warnings to be reported that are useful for discovering incompatibilities when updating ActionScript 2.0 code to ActionScri...

### `document.asVersion`
an integer that specifies which version of ActionScript is being used in the specified document. Acceptable values are 1, 2, and 3. To determine the targeted player version for the specified document, use document.getPlayerVersion(); this method returns a string, so it can be used by Flash® Lite™...

### `document.autoLabel`
a Boolean value that is equivalent to the Auto Label check box in the Accessibility panel. You can use this property to tell Flash to automatically label objects on the Stage with the text associated with them.

### `document.backgroundColor`
the color of the background, in one of the following formats:  A string in the format "#RRGGBB" or "#RRGGBBAA"  A hexadecimal number in the format 0xRRGGBB  An integer that represents the decimal equivalent of a hexadecimal number

### `document.breakApart()`
performs a break-apart operation on the current selection.
- **params:** None.

### `document.canEditSymbol()`
indicates whether the Edit Symbols menu and functionality are enabled. This is not related to whether the selection can be edited. This method should not be used to test whether fl.getDocumentDOM().enterEditMode() is allowed.
- **params:** None.
- **returns:** A Boolean value: true if the Edit Symbols menu and functionality are available for use; false otherwise.

### `document.canRevert()`
determines whether you can use the document.revert() or fl.revertDocument() method successfully.
- **params:** None.
- **returns:** A Boolean value: true if you can use the document.revert() or fl.revertDocument() methods successfully; false otherwise.

### `document.canTestMovie()`
determines whether you can use the document.testMovie() method successfully.
- **params:** None.
- **returns:** A Boolean value: true if you can use the document.testMovie() method successfully: false otherwise.

### `document.canTestScene()`
determines whether you can use the document.testScene() method successfully.
- **params:** None.
- **returns:** A Boolean value: true if you can use the document.testScene() method successfully; false otherwise.

### `document.changeFilterOrder(oldIndex, newIndex)`
changes the index of the filter in the Filters list. Any filters above or below newIndex are shifted up or down accordingly. For example, using the filters shown below, if you issue the command fl.getDocumentDOM().changeFilterOrder (3, 0), the filters are rearranged as follows: If you then issue ...
- **params:** oldIndex An integer that represents the current zero-based index position of the filter you want to reposition in the Filters list. newIndex An integer that represents the new index position of the filter in the list.

### `document.clipCopy()`
copies the current selection from the document to the Clipboard. To copy a string to the Clipboard, use fl.clipCopyString().
- **params:** None.

### `document.clipCut()`
cuts the current selection from the document and writes it to the Clipboard.
- **params:** None.

### `document.clipPaste([bInPlace])`
pastes the contents of the Clipboard into the document.
- **params:** bInPlace A Boolean value that, when set to true, causes the method to perform a paste-in-place operation. The default value is false, which causes the method to perform a paste operation to the center of the document. This parameter is optional.

### `document.close([bPromptToSaveChanges])`
closes the specified document.
- **params:** bPromptToSaveChanges A Boolean value that, when set to true, causes the method to prompt the user with a dialog box if there are unsaved changes in the document. If bPromptToSaveChanges is set to false, the user is not prompted to save any changed documents. The default value is true. This parameter is optional.

### `document.convertLinesToFills()`
converts lines to fills on the selected objects.
- **params:** None.

### `document.convertSelectionToBitmap()`
converts selected objects in the current frame to a bitmap and inserts the bitmap into the library.
- **params:** None
- **returns:** Boolean.

### `document.convertToSymbol(type, name, registrationPoint)`
converts the selected Stage item(s) to a new symbol. For information on defining linkage and shared asset properties for a symbol, see Item object.
- **params:** type A string that specifies the type of symbol to create. Acceptable values are "movie clip", "button", and "graphic". name A string that specifies the name for the new symbol, which must be unique. You can submit an empty string to have this method create a unique symbol name for you. registration point Specifies the point that represents the 0,0 location for the symbol. Acceptable values are: "top left", "top center", "top right", "center l...
- **returns:** An object for the newly created symbol, or null if it cannot create the symbol.

### `document.crop()`
uses the top selected drawing object to crop all selected drawing objects underneath it. If no objects are selected, calling this method results in an error and the script breaks at that point.
- **params:** None.
- **returns:** None.

### `document.currentPublishProfile`
a string that specifies the name of the active publish profile for the specified document.

### `document.currentTimeline`
an integer that specifies the index of the active timeline. You can set the active timeline by changing the value of this property; the effect is almost equivalent to calling document.editScene(). The only difference is that you don’t get an error message if the index of the timeline is not valid...

### `document.DebugMovie([Boolean abortIfErrorsExist])`
Invokes the Debug Movie command on the document.
- **params:** abortIfErrorsExist Boolean; the default value is false. If set to true, the debug session will not start and the .swf window will not open if there are compiler errors. Compiler warnings will not abort the command.

### `document.deleteEnvelope()`
deletes the envelope (bounding box that contains one or more objects) from the selected objects. If no objects are selected, calling this method results in an error and the script breaks at that point.
- **params:** None.
- **returns:** None.

### `document.deletePublishProfile()`
deletes the currently active profile, if there is more than one. There must be at least one profile left.
- **params:** None.
- **returns:** An integer that is the index of the new current profile. If a new profile is not available, the method leaves the current profile unchanged and returns its i...

### `document.deleteScene()`
deletes the current scene (Timeline object) and, if the deleted scene was not the last one, sets the next scene as the current Timeline object. If the deleted scene was the last one, it sets the first object as the current Timeline object. If only one Timeline object (scene) exists, it returns th...
- **params:** None.
- **returns:** A Boolean value: true if the scene is successfully deleted; false otherwise.

### `document.deleteSelection()`
deletes the current selection on the Stage. Displays an error message if there is no selection.
- **params:** None.

### `document.description`
a string that is equivalent to the Description field in the Accessibility panel. The description is read by the screen reader.

### `document.disableAllFilters()`
disables all filters on the selected objects.
- **params:** None.

### `document.disableFilter(filterIndex)`
disables the specified filter in the Filters list.
- **params:** filterIndex An integer representing the zero-based index of the filter in the Filters list.

### `document.disableOtherFilters(enabledFilterIndex)`
disables all filters except the one at the specified position in the Filters list.
- **params:** enabledFilterIndex An integer representing the zero-based index of the filter that should remain enabled after other filters are disabled.

### `document.distribute(distributemode [, bUseDocumentBounds])`
distributes the selection.
- **params:** distributemode A string that specifies where to distribute the selected objects. Acceptable values are "left edge", "horizontal center", "right edge", "top edge", "vertical center", and "bottom edge". bUseDocumentBounds A Boolean value that, when set to true, distributes the selected objects using the bounds of the document. Otherwise, the method uses the bounds of the selected objects. The default is false.

### `document.distributeToKeyframes()`
performs a distribute-to-keyframes operation on the current selection—equivalent to selecting Distribute to KeyFrames. A new keyframe is created for every object. New keyframes are created on the active layer immediately after the active frame
- **params:** None.

### `document.distributeToLayers()`
performs a distribute-to-layers operation on the current selection—equivalent to selecting Distribute to Layers. This method displays an error if there is no selection.
- **params:** None.

### `document.docClass`
a string that specifies the top-level ActionScript 3.0 class associated with the document. If the document isn’t configured to use ActionScript 3.0, this property is ignored.

### `document.documentHasData(name)`
checks the document for persistent data with the specified name.
- **params:** name A string that specifies the name of the data to check.
- **returns:** A Boolean value: true if the document has persistent data; false otherwise.

### `document.duplicatePublishProfile([profileName])`
duplicates the currently active profile and gives the duplicate version focus.
- **params:** profileName A string that specifies the unique name of the duplicated profile. If you do not specify a name, the method uses the default name. This parameter is optional.
- **returns:** An integer that is the index of the new profile in the profile list. Returns -1 if the profile cannot be duplicated.

### `document.duplicateScene()`
makes a copy of the currently selected scene, giving the new scene a unique name and making it the current scene.
- **params:** None.
- **returns:** A Boolean value: true if the scene is duplicated successfully; false otherwise.

### `document.duplicateSelection()`
duplicates the selection on the Stage.
- **params:** None.

### `document.editScene(index)`
makes the specified scene the currently selected scene for editing.
- **params:** index A zero-based integer that specifies which scene to edit.

### `document.enableAllFilters()`
enables all the filters on the Filters list for the selected objects.
- **params:** None.

### `document.enableFilter(filterIndex)`
enables the specified filter for the selected objects.
- **params:** filterIndex An integer specifying the zero-based index of the filter in the Filters list to enable.

### `document.enterEditMode([editMode])`
switches the authoring tool into the editing mode specified by the parameter. If no parameter is specified, the method defaults to symbol-editing mode, which has the same result as right-clicking the symbol to invoke the context menu and selecting Edit.
- **params:** editMode A string that specifies the editing mode. Acceptable values are "inPlace" or "newWindow". If no parameter is specified, the default is symbol-editing mode. This parameter is optional.

### `document.exitEditMode()`
exits from symbol-editing mode and returns focus to the next level up from the editing mode. For example, if you are editing a symbol inside another symbol, this method takes you up a level from the symbol you are editing, into the parent symbol.
- **params:** None.

### `document.exportInstanceToLibrary(frameNumber, bitmapName)`
Exports a selected instance of a movie clip, graphic, or button symbol on the Stage to a bitmap in Library.
- **params:** frameNumber Integer indicating the frame to be exported. bitmapName A string representing the name of the bitmap to be added to the Library.

### `document.exportInstanceToPNGSequence(outputURI, startFrameNum, endFrameNum, matrix)`
Exports a selected instance of a movie clip, graphic, or button symbol on the Stage to a series of PNG files on disk. If no startFrameNum or endFrameNum is given, the output includes all frames in the Timeline.
- **params:** outputURI String: The URI to export the PNG Sequence files to. This URI must reference a local file. Example: file:///c|/tests/mytest.png. startFrameNum Optional. An integer indicating the first frame to be exported. The default is 1. endFrameNum Optional. An Integer indicating the last frame to be exported. The default is 99999. matrix Optional. A matrix to be appended to the exported PNG sequence.

### `document.exportPNG([fileURI [, bCurrentPNGSettings [, bCurrentFrame]]])`
exports the document as one or more PNG files. If fileURI is specified and the file already exists, it is overwritten without warning. Note: If fileURI is empty and bCurrentFrame is true , the Export Movie dialog box does not display and Flash saves the exported PNG file in the same location as t...
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the filename for the exported file. If fileURI is an empty string or is not specified, Flash displays the Export Movie dialog box. bCurrentPNGSettings A Boolean value that specifies whether to use the current PNG publish settings (true) or to display the Export PNG dialog box (false). This parameter is optional. The default value is false. bCurrentFrame A Boolean value that specifie...
- **returns:** A Boolean value of true if the file is successfully exported as a PNG file; false otherwise.

### `document.exportPublishProfile(fileURI)`
exports the currently active profile to an XML file.
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the path of the XML file to which the profile is exported.

### `document.exportPublishProfileString( [profileName] )`
Method: returns a string that specifies, in XML format, the specified profile. If you don’t pass a value for profileName, the current profile is exported.
- **params:** profileName A string that specifies the name of the profile to export to an XML string. This parameter is optional.
- **returns:** An XML string.

### `document.exportSWF([fileURI [, bCurrentSettings]])`
exports the document in the Flash SWF format.
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the name of the exported file. If fileURI is empty or not specified, Flash displays the Export Movie dialog box. This parameter is optional. bCurrentSettings A Boolean value that, when set to true, causes Flash to use current SWF publish settings. Otherwise, Flash displays the Export Flash Player dialog box. The default is false. This parameter is optional.

### `exportVideo( fileURI [, convertInAdobeMediaEncoder] [, transparent] [, stopAtFrame] [, stopAtFrameOrTime] )`
exports a video from the document and optionally sends it to Adobe Media Encoder to convert the video.
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the fully qualified path to which the video is saved. convertInAdobeMediaEncoder A boolen value that specifies whether or not to send the recorded video to Adobe Media Encoder. The default value is true, which sends the video to Adobe Media Encoder. This parameter is optional. transparent A boolean value that specifies whether or not the background should be included in the video. T...

### `document.externalLibraryPath`
a string that contains a list of items in the document’s ActionScript 3.0 External library path, which specifies the location of SWC files used as runtime shared libraries. Items in the string are delimited by semi-colons. In the authoring tool, the items are specified by choosing File > Publish ...

### `document.forceSimple`
a Boolean value that specifies whether the children of the specified object are accessible. This is equivalent to the inverse logic of the Make Child Objects Accessible setting in the Accessibility panel. That is, if forceSimple is true, it is the same as the Make Child Object Accessible option b...

### `document.frameRate`
a float value that specifies the number of frames displayed per second when the SWF file plays; the default is 12. Setting this property is the same as setting the default frame rate in the Document Properties dialog box (Modify > Document) in the FLA file.

### `document.getAlignToDocument()`
identical to retrieving the value of the To Stage button in the Align panel. Gets the preference that can be used for document.align(), document.distribute(), document.match(), and document.space() methods on the document.
- **params:** None.
- **returns:** A Boolean value: true if the preference is set to align the objects to the Stage; false otherwise.

### `document.getBlendMode()`
returns a string that specifies the blending mode for the selected objects.
- **params:** None.
- **returns:** A string that specifies the blending mode for the selected objects. If more than one object is selected and they have different blending modes, the string re...

### `document.getCustomFill([objectToFill])`
retrieves the fill object of the selected shape or, if specified, of the Tools panel and Property inspector.
- **params:** objectToFill A string that specifies the location of the fill object. The following values are valid:  "toolbar" returns the fill object of the Tools panel and Property inspector.  "selection" returns the fill object of the selection. If you omit this parameter, the default value is "selection". If there is no selection, the method returns undefined. This parameter is optional.
- **returns:** The Fill object specified by the objectToFill parameter, if successful; otherwise, it returns undefined.

### `document.getCustomStroke([locationOfStroke])`
Returns the stroke object of the selected shape or, if specified, of the Tools panel and Property inspector.
- **params:** locationOfStroke A string that specifies the location of the stroke object. The following values are valid:  "toolbar", if set, returns the stroke object of the Tools panel and Property inspector.  "selection", if set, returns the stroke object of the selection. If you omit this parameter, it defaults to "selection". If there is no selection, it returns undefined. This parameter is optional.
- **returns:** The Stroke object specified by the locationOfStroke parameter, if successful; otherwise, it returns undefined.

### `document.getDataFromDocument(name)`
retrieves the value of the specified data. The type returned depends on the type of data that was stored.
- **params:** name A string that specifies the name of the data to return.
- **returns:** The specified data.

### `document.getElementProperty(propertyName)`
gets the specified Element property for the current selection. For a list of acceptable values, see the Property summary table for the Element object.
- **params:** propertyName A string that specifies the name of the Element property for which to retrieve the value.
- **returns:** The value of the specified property. Returns null if the property is an indeterminate state, as when multiple elements are selected with different property v...

### `document.getElementTextAttr(attrName [, startIndex [, endIndex]])`
gets a specific TextAttrs property of the selected Text objects. Selected objects that are not text fields are ignored. For a list of property names and expected values, see the Property summary table for the TextAttrs object. See also document.setElementTextAttr().
- **params:** attrName A string that specifies the name of the TextAttrs property to be returned. For a list of property names and expected values, see the Property summary table for the TextAttrs object. startIndex An integer that specifies the index of first character, with 0 (zero) specifying the first position. This parameter is optional. endIndex An integer that specifies the index of last character. This parameter is optional.
- **returns:** If one text field is selected, the property is returned if there is only one value used within the text. Returns undefined if there are several values used i...

### `document.getFilters()`
returns an array that contains the list of filters applied to the currently selected objects. If multiple objects are selected and they don’t have identical filters, this method returns the list of filters applied to the first selected object.
- **params:** None.
- **returns:** An array that contains a list of filters applied to the currently selected objects.

### `document.getMetadata()`
returns a string containing the XML metadata associated with the document, or an empty string if there is no metadata.
- **params:** None.
- **returns:** A string containing the XML metadata associated with the document or an empty string if there is no metadata.

### `document.getMobileSettings()`
returns the mobile XML settings for the document.
- **params:** None.
- **returns:** A string that represents the XML settings for the document. If no value has been set, returns an empty string.

### `document.getPlayerVersion()`
returns a string that represents the targeted player version for the specified document. For a list of values that this method can return, see document.setPlayerVersion(). To determine which version of ActionScript is being targeted in the specified file, use document.asVersion.
- **params:** None.
- **returns:** A string that represents the Flash Player version specified by using document.setPlayerVersion(). If no value has been set, returns the value specified in th...

### `document.getPublishDocumentData(format)`
Indicates whether publishing of the specified persistent data is enabled for the specified format in this document.
- **params:** format A string that specifies the publishing format. Note: _EMBED_SWF_ is a special built-in publishing format for persistent data. If set, the persistent data will be embedded in the SWF file every time a document is published. The persistent data can then be accessed via ActionScript with the .metaData property. This requires SWF version 19 (Flash Player 11.6) and above and is only for symbol instances onstage. Other custom publishing forma...
- **returns:** Boolean; True if publishing of the specified persistent data is enabled for the specified format in this document. Otherwise False.

### `document.getSWFPathFromProfile()`
gets the path to the SWF file that is set in the current Publish profile.
- **params:** None.
- **returns:** The full path to the SWF file that is set in the current Publish profile.

### `document.getSelectionRect()`
gets the bounding rectangle of the current selection. If a selection is non-rectangular, the smallest rectangle encompassing the entire selection is returned. The rectangle is based on the document space or, when in edit mode, the registration point (also origin point or zero point) of the symbol...
- **params:** None.
- **returns:** The bounding rectangle of the current selection, or 0 if nothing is selected. For information on the format of the return value, see document.addNewRectangle().

### `document.getTelemetryForSwf( )`
Indicates whether if the “Enable detailed telemetry” checkbox is selected in the Publish Settings dialog.
- **params:** None.
- **returns:** Returns boolean. Returns true if the “Enable detailed telemetry” checkbox is selected; otherwise false.

### `document.getTextString([startIndex [, endIndex]])`
gets the currently selected text. If the optional parameters are not passed, the current text selection is used. If text is not currently opened for editing, the whole text string is returned. If only startIndex is passed, the string starting at that index and ending at the end of the field is re...
- **params:** startIndex An integer that is an index of first character to get. This parameter is optional. endIndex An integer that is an index of last character to get. This parameter is optional.
- **returns:** A string that contains the selected text.

### `document.getTimeline()`
retrieves the current Timeline object in the document. The current timeline can be the current scene, the current symbol being edited, or the current screen.
- **params:** None.
- **returns:** The current Timeline object.

### `document.getTransformationPoint()`
gets the location of the transformation point of the current selection. You can use the transformation point for commutations such as rotate and skew. Note: Transformation points are relative to different locations, depending on the type of item selected. For more information, see document.setTra...
- **params:** None.
- **returns:** A point (for example, {x:10, y:20}, where x and y are floating-point numbers) that specifies the position of the transformation point (also origin point or z...

### `document.group()`
converts the current selection to a group.
- **params:** None.

### `document.height`
an integer that specifies the height of the document (Stage) in pixels.

### `document.id`
a unique integer (assigned automatically) that identifies a document during a Flash session. Use this property in conjunction with fl.findDocumentDOM() to specify a particular document for an action.

### `document.importFile(fileURI [, importToLibrary [, showDialog [, showImporterUI ]]])`
imports a file into a document. This method performs the same operation as the Import To Library or Import To Stage menu command. To import a publish profile, use document.importPublishProfile().
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the path of the file to import. importToLibrary A Boolean value that specifies whether to import the file only into the document’s library (true) or to also place a copy on the Stage (false). The default value is false. showDialog A Boolean value that specifies whether to display the Import dialog box. Specifying true displays the import dialog. If you specify false, the function im...

### `document.importPublishProfile( fileURI )`
imports a profile from a file.
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the path of the XML file defining the profile to import.
- **returns:** An integer that is the index of the imported profile in the profiles list. Returns -1 if the profile cannot be imported.

### `document.importPublishProfileString(xmlString)`
Method: imports an XML string that represents a publish profile and sets it as the current profile. To generate an XML string to import, use document.exportPublishProfileString() before using this method.
- **params:** xmlString A string that contains the XML data to be imported as the current profile.
- **returns:** A Boolean value of true if the string was successfully imported; false otherwise.

### `document.intersect()`
creates an intersection drawing object from all selected drawing objects. If no objects are selected, calling this method results in an error and the script breaks at that point.
- **params:** None.
- **returns:** None.

### `document.library`
the library object for a document.

### `document.libraryPath`
a string that contains a list of items in the document’s ActionScript 3.0 Library path, which specifies the location of SWC files or folders containing SWC files. Items in the string are delimited by semi-colons. In the authoring tool, the items are specified by choosing File > Publish Settings a...

### `document.livePreview`
a Boolean value that specifies whether Live Preview is enabled. If set to true, components appear on the Stage as they will appear in the published Flash content, including their approximate size. If set to false, components appear only as outlines. The default value is true.
- **params:** URI String; the absolute path to the cue point XML file.

### `document.match(bWidth, bHeight [, bUseDocumentBounds])`
makes the size of the selected objects the same.
- **params:** bWidth A Boolean value that, when set to true, causes the method to make the widths of the selected items the same. bHeight A Boolean value that, when set to true, causes the method to make the heights of the selected items the same. bUseDocumentBounds A Boolean value that, when set to true, causes the method to match the size of the objects to the bounds of the document. Otherwise, the method uses the bounds of the largest object. The default...

### `document.mouseClick(position, bToggleSel, bShiftSel)`
performs a mouse click from the Selection tool.
- **params:** position A pair of floating-point values that specify the x and y coordinates of the click in pixels. bToggleSel A Boolean value that specifies the state of the Shift key: true for pressed; false for not pressed. bShiftSel A Boolean value that specifies the state of the application preference Shift select: true for on; false for off.

### `document.mouseDblClk(position, bAltDown, bShiftDown, bShiftSelect)`
performs a double mouse click from the Selection tool.
- **params:** position A pair of floating-point values that specify the x and y coordinates of the click in pixels. bAltdown A Boolean value that records whether the Alt key is down at the time of the event: true for pressed; false for not pressed. bShiftDown A Boolean value that records whether the Shift key was down when the event occurred: true for pressed; false for not pressed. bShiftSelect A Boolean value that indicates the state of the application pr...

### `document.moveSelectedBezierPointsBy(delta)`
if the selection contains at least one path with at least one Bézier point selected, moves all selected Bézier points on all selected paths by the specified amount.
- **params:** delta A pair of floating-point values that specify the x and y coordinates in pixels by which the selected Bézier points are moved. For example, passing ({x:1,y:2}) specifies a location that is to the right by one pixel and down by two pixels from the current location.

### `document.moveSelectionBy(distanceToMove)`
moves selected objects by a specified distance. Note: When the user uses the arrow keys to move the item, the History panel combines all presses of the arrow key as one move step. When the user presses the arrow keys repeatedly, rather than taking multiple steps in the History panel, the method p...
- **params:** distanceToMove A pair of floating-point values that specify the x and y coordinate values by which the method moves the selection. For example, passing ({x:1,y:2}) specifies a location one pixel to the right and two pixels down from the current location.

### `document.name`
a string that represents the name of a document (FLA file).

### `document.optimizeCurves(smoothing, bUseMultiplePasses)`
optimizes smoothing for the current selection, allowing multiple passes, if specified, for optimal smoothing. This method is equivalent to selecting Modify > Shape > Optimize.
- **params:** smoothing An integer in the range from 0 to 100, with 0 specifying no smoothing and 100 specifying maximum smoothing. bUseMultiplePasses A Boolean value that, when set to true, indicates that the method should use multiple passes, which is slower but produces a better result. This parameter has the same effect as clicking the Use Multiple Passes button in the Optimize Curves dialog box.

### `document.path`
a string that represents the path of the document in a platform-specific format. If the document has never been saved, this property is undefined.

### `document.pathURI`
a string that represents the path of the document, expressed as a file:/// URI. If the document has never been saved, this property is undefined.

### `document.publish()`
publishes the document according to the active publish settings (File > Publish Settings). This method is equivalent to selecting File > Publish.
- **params:** None.

### `document.publishProfiles`
an array of the publish profile names for the document.

### `document.punch()`
uses the top selected drawing object to punch through all selected drawing objects underneath it. If no objects are selected, calling this method results in an error and the script breaks at that point.
- **params:** None.
- **returns:** None.

### `document.removeAllFilters()`
removes all filters from the selected objects.
- **params:** None.

### `document.removeDataFromDocument(name)`
removes persistent data with the specified name that has been attached to the document.
- **params:** name A string that specifies the name of the data to remove.

### `document.removeDataFromSelection(name)`
removes persistent data with the specified name that has been attached to the selection.
- **params:** name A string that specifies the name of the persistent data to remove.

### `document.removeFilter(filterIndex)`
removes the specified filter from the Filters list of the selected objects.
- **params:** filterIndex An integer specifying the zero-based index of the filter to remove from the selected objects.

### `document.renamePublishProfile([profileNewName])`
renames the current profile.
- **params:** profileNewName An optional parameter that specifies the new name for the profile. The new name must be unique. If the name is not specified, a default name is provided.
- **returns:** A Boolean value: true if the name is changed successfully; false otherwise.

### `document.renameScene(name)`
renames the currently selected scene in the Scenes panel. The new name for the selected scene must be unique.
- **params:** name A string that specifies the new name of the scene.
- **returns:** A Boolean value: true if the name is changed successfully; false otherwise. If the new name is not unique, for example, the method returns false.

### `document.reorderScene(sceneToMove, sceneToPutItBefore)`
moves the specified scene before another specified scene.
- **params:** sceneToMove An integer that specifies which scene to move, with 0 (zero) being the first scene. sceneToPutItBefore An integer that specifies the scene before which you want to move the scene specified by sceneToMove. Specify 0 (zero) for the first scene. For example, if you specify 1 for sceneToMove and 0 for sceneToPutItBefore, the second scene is placed before the first scene. Specify -1 to move the scene to the end.

### `document.resetOvalObject()`
sets all values in the Property inspector to default Oval object settings. If any Oval objects are selected, their properties are reset to default values as well.
- **params:** None.

### `document.resetRectangleObject()`
sets all values in the Property inspector to default Rectangle object settings. If any Rectangle objects are selected, their properties are reset to default values as well.
- **params:** None.

### `document.resetTransformation()`
resets the transformation matrix. This method is equivalent to selecting Modify > Transform > Remove Transform.
- **params:** None.

### `document.revert()`
reverts the specified document to its previously saved version. This method is equivalent to selecting File > Revert.
- **params:** None.

### `document.rotate3DSelection(xyzCoordinate, bGlobalTransform)`
Method: applies a 3D rotation to the selection. This method is available only for movie clips.
- **params:** xyzCoordinate An XYZ coordinate point that specifies the axes for 3D rotation. bGlobalTransform A Boolean value that specifies whether the transformation mode should be global (true) or local (false).

### `document.rotateSelection(angle [, rotationPoint])`
rotates the selection by a specified number of degrees. The effect is the same as using the Free Transform tool to rotate the object.
- **params:** angle A floating-point value that specifies the angle of the rotation. rotationPoint A string that specifies which side of the bounding box to rotate. Acceptable values are "top right", "top left", "bottom right", "bottom left", "top center", "right center", "bottom center", and "left center". If unspecified, the method uses the transformation point. This parameter is optional.

### `document.save([bOkToSaveAs])`
saves the document in its default location. This method is equivalent to selecting File > Save. To specify a name for the file (instead of saving it with the same name), use fl.saveDocument(). Note: If the file is new and has not been modified or saved, or if the file has not been modified since ...
- **params:** bOkToSaveAs An optional parameter that, if true or omitted, and the file was never saved, opens the Save As dialog box. If false and the file was never saved, the file is not saved.
- **returns:** A Boolean value: true if the save operation completes successfully; false otherwise.

### `document.saveAsCopy(URI [, selectionOnly])`
Saves a new FLA file based on the existing document object, with an option to save only the current selection on Stage.
- **params:** URI String: The URI to export the new FLA file to. This URI must reference a local file. Example: file:///c|/tests/myTest.fla. selectionOnly Optional. A boolean indicating whether only the current Stage selection should be saved to the new FLA file.
- **returns:** Boolean.

### `document.scaleSelection(xScale, yScale [, whichCorner])`
scales the selection by a specified amount. This method is equivalent to using the Free Transform tool to scale the object.
- **params:** xScale A floating-point value that specifies the amount of x by which to scale. yScale A floating-point value that specifies the amount of y by which to scale. whichCorner A string value that specifies the edge about which the transformation occurs. If omitted, scaling occurs about the transformation point. Acceptable values are: "bottom left", "bottom right", "top right", "top left", "top center", "right center", "bottom center", and "left ce...

### `document.selectAll()`
selects all items on the Stage. This method is equivalent to pressing Control+A (Windows) or Command+A (Macintosh) or selecting Edit > Select All.
- **params:** None.

### `document.selectNone()`
deselects any selected items.
- **params:** None.

### `document.selection`
an array of the selected objects in the document. If nothing is selected, returns an array of length zero. If no document is open, returns null. To add objects to the array, you must first select them in one of the following ways:  Manually select objects on the Stage.  Use one of the selection...

### `document.setAlignToDocument(bToStage)`
sets the preferences for document.align(), document.distribute(), document.match(), and document.space() to act on the document. This method is equivalent to enabling the To Stage button in the Align panel.
- **params:** bToStage A Boolean value that, if set to true, aligns objects to the Stage. If set to false, it does not.

### `document.setBlendMode(mode)`
sets the blending mode for the selected objects.
- **params:** mode A string that represents the desired blending mode for the selected objects. Acceptable values are "normal", "layer", "multiply", "screen", "overlay", "hardlight", "lighten", "darken", "difference", "add", "subtract", "invert", "alpha", and "erase".

### `document.setCustomFill(fill)`
sets the fill settings for the Tools panel, Property inspector, and any selected shapes. This allows a script to set the fill settings before drawing the object, rather than drawing the object, selecting it, and changing the fill settings. It also lets a script change the Tools panel and Property...
- **params:** fill A Fill object that specifies the fill settings to be used. See Fill object.

### `document.setCustomStroke(stroke)`
sets the stroke settings for the Tools panel, Property inspector, and any selected shapes. This allows a script to set the stroke settings before drawing the object, rather than drawing the object, selecting it, and changing the stroke settings. It also lets a script change the Tools panel and Pr...
- **params:** stroke A Stroke object.

### `document.setElementProperty(property, value)`
sets the specified Element property on selected objects in the document. This method does nothing if there is no selection.
- **params:** property A string that specifies the name of the Element property to set. For a complete list of properties and values, see the Property summary table for the Element object. You can’t use this method to set values for read-only properties, such as element.elementType, element.top, or element.left. value An integer that specifies the value to set in the specified Element property.

### `document.setElementTextAttr(attrName, attrValue [, startIndex [, endIndex]])`
sets the specified textAttrs property of the selected text items to the specified value. For a list of property names and allowable values, see the Property summary table for the TextAttrs object. If the optional parameters are not passed, the method sets the style of the currently selected text ...
- **params:** attrName A string that specifies the name of the TextAttrs property to change. attrValue The value to which to set the TextAttrs property. For a list of property names and expected values, see the Property summary table for the TextAttrs object. startIndex An integer value that specifies the index of the first character that is affected. This parameter is optional. endIndex An integer value that specifies the index of the last character that i...
- **returns:** A Boolean value: true if at least one text attribute property is changed; false otherwise.

### `document.setFillColor(color)`
changes the selection and the tools panel to the specified fill color. For additional information on changing the fill color in the Tools panel and Property inspector, see document.setCustomFill().
- **params:** color The color of the fill, in one of the following formats:  A string in the format "#RRGGBB" or "#RRGGBBAA"  A hexadecimal number in the format 0xRRGGBB  An integer that represents the decimal equivalent of a hexadecimal number If set to null, no fill color is set, which is the same as setting the Fill color swatch in the user interface to no fill.

### `document.setFilterProperty(property, filterIndex, value)`
sets a specified filter property for the currently selected objects (assuming that the object supports the specified filter).
- **params:** property A string specifying the property to be set. Acceptable values are "blurX", "blurY", "quality", angle", "distance", "strength", "knockout", "inner", "bevelType", "color", "shadowColor", and "highlightColor". filterIndex An integer specifying the zero-based index of the filter in the Filters list. value A number or string specifying the value to be set for the specified filter property. Acceptable values depend on the property and the f...

### `document.setFilters(filterArray)`
applies filters to the selected objects. Use this method after calling document.getFilters() and making any desired changes to the filters.
- **params:** filterArray The array of filters currently specified.

### `document.setInstanceAlpha(opacity)`
Methods; sets the opacity of the instance.
- **params:** opacity An integer between 0 (transparent) and 100 (completely saturated) that adjusts the transparency of the instance.

### `document.setInstanceBrightness(brightness)`
sets the brightness for the instance.
- **params:** brightness An integer that specifies brightness as a value from -100 (black) to 100 (white).

### `document.setInstanceTint( color, strength )`
sets the tint for the instance.
- **params:** color The color of the tint, in one of the following formats:  A string in the format "#RRGGBB" or "#RRGGBBAA"  A hexadecimal number in the format 0xRRGGBB  An integer that represents the decimal equivalent of a hexadecimal number strength An integer between 0 and 100 that specifies the opacity of the tint.

### `document.setMetadata(strMetadata)`
sets the XML metadata for the specified document, overwriting any existing metadata. The XML passed as strMetadata is validated and may be rewritten before being stored. If it cannot be validated as legal XML or violates specific rules, then the XML metadata is not set and false is returned. (If ...
- **params:** strMetadata A string containing the XML metadata to be associated with the document. For more information, see the following description.
- **returns:** A Boolean value: true if successful; false otherwise.

### `document.setMobileSettings(xmlString)`
sets the value of an XML settings string in a mobile FLA file. (Most mobile FLA files have an XML string that describes the settings within the document.)
- **params:** xmlString A string that describes the XML settings in a mobile FLA file.
- **returns:** A value of true if the settings were successfully set; false otherwise.

### `document.setOvalObjectProperty(propertyName, value)`
specifies a value for a specified property of primitive Oval objects.
- **params:** propertyName A string that specifies the property to be set. For acceptable values, see the Property summary table for the Oval object. value The value to be assigned to the property. Acceptable values vary depending on the property you specify in propertyName.

### `document.setPlayerVersion(version)`
sets the version of the Flash Player targeted by the specified document. This is the same value as that set in the Publish Settings dialog box.
- **params:** version A string that represents the version of Flash Player targeted by the specified document. Acceptable values are "FlashLite", "FlashLite11", "FlashLite20" , "FlashLite30", "1", "2", "3", "4", "5", "6", "7", "8", "9", "FlashPlayer10", "FlashPlayer10.3", "FlashPlayer11.1", "FlashPlayer11.2", "FlashPlayer11.3","FlashPlayer11.4", "FlashPlayer11.5", "FlashPlayer11.6", "FlashPlayer11.7", "AdobeAIR1_1", "AdobeAIR1_1", "AdobeAIR2_5", "AdobeAIR3_...
- **returns:** A value of true if the player version was successfully set; false otherwise.

### `document.setPublishDocumentData(format, publish)`
Enables or disables publishing of persistent data for an entire document.
- **params:** format A string that specifies the publishing format. Note: _EMBED_SWF_ is a special built-in publishing format for persistent data. If set, the persistent data will be embedded in the SWF file every time a document is published. The persistent data can then be accessed via ActionScript with the .metaData property. This requires SWF version 19 (Flash Player 11.6) and above and is only for symbol instances onstage. Other custom publishing forma...
- **returns:** None.

### `document.setRectangleObjectProperty(propertyName, value)`
specifies a value for a specified property of primitive Rectangle objects.
- **params:** propertyName A string that specifies the property to be set. For acceptable values, see the Property summary table for the Rectangle object. value The value to be assigned to the property. Acceptable values vary depending on the property you specify in propertyName.

### `document.setSelectionBounds(boundingRectangle [, bContactSensitiveSelection])`
moves and resizes the selection in a single operation. If you pass a value for bContactSensitiveSelection, it is valid only for this method and doesn’t affect the Contact Sensitive selection mode for the document (see fl.contactSensitiveSelection).
- **params:** boundingRectangle A rectangle that specifies the new location and size of the selection. For information on the format of boundingRectangle, see document.addNewRectangle(). bContactSensitiveSelection A Boolean value that specifies whether the Contact Sensitive selection mode is enabled (true) or disabled (false) during object selection. The default value is false.

### `document.setSelectionRect(rect [, bReplaceCurrentSelection [, bContactSensitiveSelection]])`
draws a rectangular selection marquee relative to the Stage, using the specified coordinates. This is unlike document.getSelectionRect(), in which the rectangle is relative to the object being edited. This method is equivalent to dragging a rectangle with the Selection tool. An instance must be f...
- **params:** rect A rectangle object to set as selected. For information on the format of rect, see document.addNewRectangle(). bReplaceCurrentSelection A Boolean value that specifies whether the method replaces the current selection (true) or adds to the current selection (false). The default value is true. bContactSensitiveSelection A Boolean value that specifies whether the Contact Sensitive selection mode is enabled (true) or disabled (false) during ob...

### `document.setStageVanishingPoint(point)`
Specifies the vanishing point for viewing 3D objects.
- **params:** point A point that specifies the x and y coordinates of the location at which to set the vanishing point for viewing 3D objects.

### `document.setStageViewAngle(angle)`
Specifies the perspective angle for viewing 3D objects.
- **params:** angle A floating point value between 0.0 and 179.0.

### `document.setStroke(color, size, strokeType)`
sets the color, width, and style of the selected stroke. For information on changing the stroke in the Tools panel and Property inspector, see document.setCustomStroke().
- **params:** color The color of the stroke, in one of the following formats:  A string in the format "#RRGGBB" or "#RRGGBBAA"  A hexadecimal number in the format 0xRRGGBB  An integer that represents the decimal equivalent of a hexadecimal number size A floating-point value that specifies the new stroke size for the selection. strokeType A string that specifies the new type of stroke for the selection. Acceptable values are "hairline", "solid", "dashed",...

### `document.setStrokeColor(color)`
changes the stroke color of the selection to the specified color. For information on changing the stroke in the Tools panel and Property inspector, see document.setCustomStroke().
- **params:** color The color of the stroke, in one of the following formats:  A string in the format "#RRGGBB" or "#RRGGBBAA"  A hexadecimal number in the format 0xRRGGBB  An integer that represents the decimal equivalent of a hexadecimal number

### `document.setStrokeSize(size)`
changes the stroke size of the selection to the specified size. For information on changing the stroke in the Tools panel and Property inspector, see document.setCustomStroke().
- **params:** size A floating-point value from 0.25 to 250that specifies the stroke size. The method ignores precision greater than two decimal places.

### `document.setStrokeStyle(strokeType)`
changes the stroke style of the selection to the specified style. For information on changing the stroke in the Tools panel and Property inspector, see document.setCustomStroke().
- **params:** strokeType A string that specifies the stroke style for the current selection. Acceptable values are "hairline", "solid","dashed", "dotted", "ragged", "stipple", and "hatched".

### `document.setTextRectangle(boundingRectangle)`
changes the bounding rectangle for the selected text item to the specified size. This method causes the text to reflow inside the new rectangle; the text item is not scaled or transformed. The values passed in boundingRectangle are used as follows:  If the text is horizontal and static, the meth...
- **params:** boundingRectangle A rectangle that specifies the new size within which the text item should flow. For information on the format of boundingRectangle, see document.addNewRectangle().
- **returns:** A Boolean value: true if the size of at least one text field is changed; false otherwise.

### `document.setTextSelection(startIndex, endIndex)`
sets the text selection of the currently selected text field to the values specified by the startIndex and endIndex values. Text editing is activated, if it isn’t already.
- **params:** startIndex An integer that specifies the position of the first character to select. The first character position is 0 (zero). endIndex An integer that specifies the end position of the selection up to, but not including, endIndex. The first character position is 0 (zero).
- **returns:** A Boolean value: true if the method can successfully set the text selection; false otherwise.

### `document.setTextString(text [, startIndex [, endIndex]])`
inserts a string of text. If the optional parameters are not passed, the existing text selection is replaced; if the Text object isn’t currently being edited, the whole text string is replaced. If only startIndex is passed, the string passed is inserted at this position. If startIndex and endInde...
- **params:** text A string of the characters to insert in the text field. startIndex An integer that specifies the first character to replace. The first character position is 0 (zero). This parameter is optional. endIndex An integer that specifies the last character to replace. This parameter is optional.
- **returns:** A Boolean value: true if the text of at least one text string is set; false otherwise.

### `document.setTransformationPoint( transformationPoint )`
sets the position of the current selection’s transformation point.
- **params:** transformationPoint A point (for example, {x:10, y:20}, where x and y are floating-point numbers) that specifies values for the transformation point of each of the following elements:  Shapes: transformationPoint is set relative to the document (0,0 is the upper left corner of the Stage).  Symbols: transformationPoint is set relative to the symbol’s registration point (0,0 is located at the registration point).  Text: transformationPoint is...

### `document.silent`
a Boolean value that specifies whether the object is accessible. This is equivalent to the inverse logic of the Make Movie Accessible setting in the Accessibility panel. That is, if document.silent is true, it is the same as the Make Movie Accessible option being unchecked. If it is false, it is ...

### `document.skewSelection(xSkew, ySkew [, whichEdge])`
skews the selection by a specified amount. The effect is the same as using the Free Transform tool to skew the object.
- **params:** xSkew A floating-point number that specifies the amount of x by which to skew, measured in degrees. ySkew A floating-point number that specifies the amount of y by which to skew, measured in degrees. whichEdge A string that specifies the edge where the transformation occurs; if omitted, skew occurs at the transformation point. Acceptable values are "top center", "right center", "bottom center", and "left center". This parameter is optional.

### `document.smoothSelection()`
smooths the curve of each selected fill outline or curved line. This method performs the same action as the Smooth button in the Tools panel.
- **params:** None.

### `document.sourcePath`
a string that contains a list of items in the document’s ActionScript 3.0 Source path, which specifies the location of ActionScript class files. Items in the string are delimited by semi-colons. In the authoring tool, the items are specified by choosing File > Publish Settings and then choosing A...

### `document.space(direction [, bUseDocumentBounds])`
spaces the objects in the selection evenly.
- **params:** direction A string that specifies the direction in which to space the objects in the selection. Acceptable values are "horizontal" or "vertical". bUseDocumentBounds A Boolean value that, when set to true, spaces the objects to the document bounds. Otherwise, the method uses the bounds of the selected objects. The default is false. This parameter is optional.

### `document.straightenSelection()`
straightens the currently selected strokes. This method is equivalent to using the Straighten button in the Tools panel.
- **params:** None.

### `document.swapElement(name)`
swaps the current selection with the specified one. The selection must contain a graphic, button, movie clip, video, or bitmap. This method displays an error message if no object is selected or the given object could not be found.
- **params:** name A string that specifies the name of the library item to use.

### `document.swapStrokeAndFill()`
swaps the Stroke and Fill colors.
- **params:** None.

### `document.swfJPEGQuality`
an integer, returns the JPEG Quality setting from the current Publish Profile in the document.

### `document.testMovie([Boolean abortIfErrorsExist])`
executes a Test Movie operation on the document.
- **params:** abortIfErrorsExist Boolean; the default value is false. If set to true, the test movie session will not start and the .swf window will not open if there are compiler errors. Compiler warnings will not abort the command. This parameter was added in Flash Professional CS5.

### `document.testScene()`
executes a Test Scene operation on the current scene of the document.
- **params:** None.

### `document.timelines`
an array of Timeline objects (see Timeline object).

### `document.traceBitmap(threshold, minimumArea, curveFit, cornerThreshold)`
performs a trace bitmap on the current selection. This method is equivalent to selecting Modify > Bitmap > Trace Bitmap.
- **params:** threshold An integer that controls the number of colors in your traced bitmap. Acceptable values are integers between 0 and 500. minimumArea An integer that specifies the radius measured in pixels. Acceptable values are integers between 1 and 1000. curveFit A string that specifies how smoothly outlines are drawn. Acceptable values are "pixels", "very tight", "tight", "normal", "smooth", and "very smooth". cornerThreshold A string that is simil...

### `document.transformSelection(a, b, c, d)`
performs a general transformation on the current selection by applying the matrix specified in the arguments. For more information, see the element.matrix property.
- **params:** a A floating-point number that specifies the (0,0) element of the transformation matrix. b A floating-point number that specifies the (0,1) element of the transformation matrix. c A floating-point number that specifies the (1,0) element of the transformation matrix. d A floating-point number that specifies the (1,1) element of the transformation matrix.

### `document.translate3DCenter(xyzCoordinate)`
Method: sets the XYZ position around which the selection is translated or rotated. This method is available only for movie clips.
- **params:** xyzCoordinate An XYZ coordinate that specifies the center point for 3D rotation or translation.

### `document.translate3DSelection(xyzCoordinate, bGlobalTransform)`
Method: applies a 3D translation to the selection. This method is available only for movie clips.
- **params:** xyzCoordinate An XYZ coordinate that specifies the axes for 3D translation. bGlobalTransform A Boolean value that specifies whether the transformation mode should be global (true) or local (false).

### `document.unGroup()`
ungroups the current selection.
- **params:** None.

### `document.union()`
combines all selected shapes into a drawing object. If no objects are selected, calling this method results in an error and the script breaks at that point.
- **params:** None.
- **returns:** None.

### `document.unlockAllElements()`
unlocks all locked elements on the currently selected frame.
- **params:** None.

### `document.viewMatrix`
a Matrix object. The viewMatrix is used to transform from object space to document space when the document is in edit mode. The mouse location, as a tool receives it, is relative to the object that is currently being edited. See Matrix object. For example, if you create a symbol, double-click to ...

### `document.width`
an integer that specifies the width of the document (Stage) in pixels.

### `document.xmlPanel(fileURI)`
posts an XMLUI dialog box. See fl.xmlui.
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the path to the XML file defining the controls in the panel. The full path is required.
- **returns:** An object that has properties defined for all controls defined in the XML file. All properties are returned as strings. The returned object will have one pre...

### `document.zoomFactor`
specifies the zoom percent of the Stage at authoring time. A value of 1 equals 100 percent zoom, 8 equals 800 percent, .5 equals 50 percent, and so on.

