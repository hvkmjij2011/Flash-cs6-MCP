
## fill  (10)

### `fill.bitmapIsClipped`
a Boolean value that specifies whether the bitmap fill for a shape that is larger than the bitmap is clipped ( true) or repeated (false). This property is available only if the value of the fill.style property is "bitmap". If the shape is smaller than the bitmap, this value is false. Property Des...

### `fill.bitmapPath`
a string that specifies the path and name of the bitmap fill in the Library. This property is available only if the value of the fill.style property is "bitmap".

### `fill.color`
the color of the fill, in one of the following formats:  A string in the format "#RRGGBB" or "#RRGGBBAA"  A hexadecimal number in the format 0xRRGGBB  An integer that represents the decimal equivalent of a hexadecimal number

### `fill.colorArray`
an array of colors in the gradient, expressed as integers. This property is available only if the value of the fill.style property is either "radialGradient" or "linearGradient". See fill.style

### `fill.focalPoint`
an integer that specifies the gradient focal point horizontal offset from the transformation point. A value of 10, for example, would place the focal point at 10/255 of the distance from the transformation point to the edge of the gradient. A value of -255 would place the focal point at the left ...

### `fill.linearRGB`
a Boolean value that specifies whether to render the fill as a linear or radial RGB gradient. Set this property to true to specify a linear interpolation of a gradient; set it to false to specify a radial interpolation of a gradient. The default value is false.

### `fill.matrix`
a Matrix object that defines the placement, orientation, and scales for gradient fills.

### `fill.overflow`
a string that specifies the behavior of a gradient’s overflow. Acceptable values are "extend", "repeat", and "reflect"; the strings are not case-sensitive. The default value is "extend".

### `fill.posArray`
an array of integers, each in the range of zero to 255, indicating the position of the corresponding color. This property is available only if the value of the fill.style property is either "radialGradient" or "linearGradient".

### `fill.style`
a string that specifies the fill style. Acceptable values are "bitmap", "solid", "linearGradient", "radialGradient", and "noFill". If this value is "linearGradient" or "radialGradient", the fill.colorArray and fill.posArray properties are also available. If this value is "bitmap", the fill.bitmap...


## fontItem  (9)

### `fontItem.bitmap`
a Boolean value that specifies whether the Font item is bitmapped (true) or not (false).

### `fontItem.bold`
a Boolean value that specifies whether the Font item is bold (true) or not (false).

### `fontItem.embedRanges`
a string value that specifies a series of delimited integers that correspond to items that can be selected in the Font Embedding dialog box. This property can also be read, allowing you to find out what characters were specified with the Font Embedding dialog box for a given Font item. Note: The ...

### `fontItem.embedVariantGlyphs`
Note: While this property is available in Flash CS5 Professional, it has no effect when applied to Text Layout Framework (TLF) text. Beginning in Flash Professional CS5, variant glyphs are always embedded in fonts used with TLF text. The flash.text.engine (FTE) referenced below is only available ...

### `fontItem.embeddedCharacters`
a string value that allows you to specify characters to embed within a SWF file so that the characters do not need to be present on the devices the SWF file eventually plays back on. This property provides the same functionality as the Font Embedding dialog box. This property can also be read, al...

### `fontItem.font`
a string that specifies the name of the device font associated with the Font item. If you enter a string that does not correspond to an installed device font, an error message is displayed. To determine if a font exists on the system, use fl.isFontInstalled(). Note: When you set this value, the r...

### `fontItem.isDefineFont4Symbol`
a Boolean value that specifies the format of the font that is output when publishing a SWF file. If this value is true, Flash outputs a font that can be used with the flash.text.engine (FTE) APIs. If this value is false, the font can be used with the flash.text APIs, including text fields. The de...

### `fontItem.italic`
a Boolean value that specifies whether the Font item is italic (true) or not (false).

### `fontItem.size`
an integer that represents the size of the Font item, in points.


## edge  (8)

### `edge.cubicSegmentIndex`
an integer that specifies the index value of a cubic segment of the edge (see shape.getCubicSegmentPoints()). Method Description edge.getControl() Gets a point object set to the location of the specified control point of the edge. edge.getHalfEdge() Returns a HalfEdge object. edge.setControl() Se...

### `edge.getControl(i)`
gets a point object set to the location of the specified control point of the edge.
- **params:** i An integer that specifies which control point of the edge to return. Specify 0 for the first control point, 1 for the middle control point, or 2 for the end control point. If the edge.isLine property is true, the middle control point is set to the midpoint of the segment joining the beginning and ending control points.
- **returns:** The specified control point.

### `edge.getHalfEdge(index)`
returns a HalfEdge object.
- **params:** index An integer that specifies which half edge to return. The value of index must be either 0 for the first half edge or 1 for the second half edge.
- **returns:** A HalfEdge object.

### `edge.id`
an integer that represents a unique identifier for the edge.

### `edge.isLine`
an integer with a value of 0 or 1. A value of 1 indicates that the edge is a straight line. In that case, the middle control point bisects the line joining the two end points.

### `edge.setControl(index, x, y)`
sets the position of the control point of the edge. You must call shape.beginEdit() before using this method. See shape.beginEdit().
- **params:** index An integer that specifies which control point to set. Use values 0, 1, or 2 to specify the beginning, middle, and end control points, respectively. x A floating-point value that specifies the horizontal location of the control point. If the Stage is in edit or edit-in-place mode, the point coordinate is relative to the edited object. Otherwise, the point coordinate is relative to the Stage. y A floating-point value that specifies the ver...

### `edge.splitEdge(t)`
splits the edge into two pieces. You must call shape.beginEdit() before using this method.
- **params:** t A floating-point value between 0 and 1 that specifies where to split the edge. A value of 0 represents one end point and a value of 1represents the other. For example, passing a value of 0.5 splits the edge in the middle, which, for a line is exactly in the center. If the edge represents a curve, 0.5 represents the parametric middle of the curve.

### `edge.stroke`
a Stroke object.


## parameter  (8)

### `parameter.category Method Description parameter.insertItem() Inserts an item into an object or array. parameter.removeItem() Removes an element of the object or array type of a screen or component parameter. Property Description parameter.category A string that specifies the category property for the screen parameter or componentInstance parameter. parameter.listIndex An integer that specifies t`
a string that specifies the category property for the screen parameter or componentInstance parameter. This property provides an alternative way of presenting a list of parameters. This functionality is not available through the Flash user interface.

### `parameter.insertItem(index, name, value, type)`
inserts an item in an object or array. If a parameter is an object or array, the value property is an array.
- **params:** index A zero-based integer index that indicates where the item will be inserted in the object or array. If the index is 0, the item is inserted at the beginning. If the index is greater than the list size, the new item is inserted at the end. name A string that specifies the name of the item to insert. This is a required parameter for object parameters. value A string that specifies the value of the item to insert. type A string that specifies...

### `parameter.listIndex`
the value of the selected list item. This property is valid only if parameter.valueType is "List".

### `parameter.name`
a string that specifies the name of the parameter.

### `parameter.removeItem(index)`
removes an element of the object or array type of a screen or component parameter.
- **params:** index The zero-based integer index of the item to be removed from the screen or component property.

### `parameter.value`
corresponds to the Value field in the Parameters tab of the Component inspector, the Parameters tab of the Property inspector, or the screen Property inspector. The type of the value property is determined by the valueType property for the parameter (see parameter.valueType). Parameter object Las...

### `parameter.valueType`
a string that indicates the type of the screen or component parameter. The type can be one of the following values: "Default", "Array", "Object", "List", "String", "Number", "Boolean", "Font Name", "Color", "Collection", "Web Service URL", or "Web Service Operation".

### `parameter.verbose`
specifies where the parameter is displayed. If the value of this property is 0 (nonverbose), the parameter is displayed only in the Component inspector. If it is 1 (verbose), the parameter is displayed in the Component inspector and in the Parameters tab of the Property inspector. 392 Chapter 32:...


## path  (8)

### `path.addCubicCurve(xAnchor, yAnchor, x2, y2, x3, y3, x4, y4) Method Description path.addCubicCurve() Appends a cubic Bézier curve segment to the path. path.addCurve() Appends a quadratic Bézier segment to the path. path.addPoint() Adds a point to the path. path.clear() Removes all points from the path. path.close() Appends a point at the location of the first point of the path and extends the pat`
appends a cubic Bézier curve segment to the path.
- **params:** xAnchor A floating-point number that specifies the x position of the first control point. yAnchor A floating-point number that specifies the y position of the first control point. x2 A floating-point number that specifies the x position of the second control point. y2 A floating-point number that specifies the y position of the second control point. x3 A floating-point number that specifies the x position of the third control point. y3 A float...

### `path.addCurve(xAnchor, yAnchor, x2, y2, x3, y3)`
appends a quadratic Bézier segment to the path.
- **params:** xAnchor A floating-point number that specifies the x position of the first control point. yAnchor A floating-point number that specifies the y position of the first control point. x2 A floating-point number that specifies the x position of the second control point. y2 A floating-point number that specifies the y position of the second control point. x3 A floating-point number that specifies the x position of the third control point. y3 A float...

### `path.addPoint(x, y)`
adds a point to the path.
- **params:** x A floating-point number that specifies the x position of the point. y A floating-point number that specifies the y position of the point.

### `path.clear()`
removes all points from the path.
- **params:** None.

### `path.close()`
appends a point at the location of the first point of the path and extends the path to that point, which closes the path. If the path has no points, no points are added.
- **params:** None.

### `path.makeShape([bSupressFill [, bSupressStroke]])`
creates a shape on the Stage by using the current stroke and fill settings. The path is cleared after the shape is created. This method has two optional parameters for suppressing the fill and stroke of the resulting shape object. If you omit these parameters or set them to false, the current val...
- **params:** bSuppressFill A Boolean value that, if set to true, suppresses the fill that would be applied to the shape. The default value is false. This parameter is optional. bSupressStroke A Boolean value that, if set to true, suppresses the stroke that would be applied to the shape. The default value is false. This parameter is optional.

### `path.nPts`
an integer representing the number of points in the path. A new path has 0 points.

### `path.newContour()`
starts a new contour in the path.
- **params:** None.


## swfPanel  (7)

### `swfPanel.call(request)`
works in conjunction with the ActionScript ExternalInterface.addCallback() and MMExecute() methods to communicate with the SWF panel from the authoring environment.
- **params:** request Parameters to pass to the function (see “Description” and “Example” below).
- **returns:** Either null or a string that is returned by the function call. The function result could be an empty string.

### `swfPanel.dpiScaleFactorX`
Read-only property: a string that contains the DPI scale factor (scaleX) for swfPanel. Depending on this scale-factor, SwfPanel can adjust its contents.

### `swfPanel.dpiScaleFactorY`
Read-only property: a string that contains the DPI scale factor (scaleY) for swfPanel. Depending on this scale-factor, SwfPanel can adjust its contents.

### `swfPanel.name`
Read-only property: a string that represents the name of the specified Window SWF panel.

### `swfPanel.path`
Read-only property: a string that represents the path to the SWF file used in the specified Window SWF panel.

### `swfPanel.reload()`
Method: Reloads content in the SWF panel.

### `swfPanel.setFocus()`
Method: Sets the keyboard focus to the specified SWF panel.


## videoItem  (7)

### `videoItem.exportToFLV(fileURI) Property Description videoItem.exportToFLV() Exports the specified item to an FLV file. Property Description videoItem.fileLastModifiedDate Read-only; a string containing a hexadecimal number that represents the number of seconds that have elapsed between January 1, 1970, and the modification date of the original file (on disk) at the time the file was imported to`
exports the specified item to an FLV file.
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the path and name of the exported file.
- **returns:** A Boolean value of true if the file is exported successfully; false otherwise.

### `videoItem.fileLastModifiedDate`
Read-only property: a string containing a hexadecimal number that represents the number of seconds that have elapsed between January 1, 1970, and the modification date of the original file (on disk) at the time the file was imported to the library. If the file no longer exists, this value is "000...

### `videoItem.lastModifiedDate`
a hexadecimal value indicating the modification date and time of the video item. This value is incremented every time the video item is imported.

### `videoItem.sourceFileExists`
Read-only property: a Boolean value of true if the file that was imported to the Library still exists in the location from where it was imported; false otherwise.

### `videoItem.sourceFileIsCurrent`
Read-only property: a Boolean value of true if the file modification date of the Library item is the same as the modification date (on disk) of the file that was imported; false otherwise.

### `videoItem.sourceFilePath`
a string, expressed as a file:/// URI that specifies the path to the video item.

### `videoItem.videoType`
a string that specifies the type of video the item represents. Possible values are "embedded video" and "video".


## actionsPanel  (6)

### `actionsPanel.getSelectedText()`
returns the text that is currently selected in the Actions panel.
- **params:** None.
- **returns:** A string that contains the text that is currently selected in the Actions panel.

### `actionsPanel.getText()`
returns the text in the Actions panel.
- **params:** None.
- **returns:** A string that contains all the text in the Actions panel.

### `actionsPanel.hasSelection()`
specifies whether any text is currently selected in the Actions panel.
- **params:** None.
- **returns:** A Boolean value that specifies whether any text is selected in the Actions panel (true) or not (false).

### `actionsPanel.replaceSelectedText(replacementText)`
replaces the currently selected text with the text specified in replacementText. If replacementText contains more characters than the selected text, any characters following the selected text now follow replacementText; that is, they are not overwritten.
- **params:** replacementText A string that represents text to replace selected text in the Actions panel.
- **returns:** A Boolean value of true if the Actions panel is found; false otherwise.

### `actionsPanel.setSelection(startIndex, numberOfChars)`
selects a specified set of characters in the Actions panel.
- **params:** startIndex A zero-based integer that specifies the first character to be selected. numberOfChars An integer that specifies how many characters to select.
- **returns:** A Boolean value that specifies whether the requested characters can be selected (true) or not (false).

### `actionsPanel.setText(replacementText)`
clears any text in the Actions panel and then adds the text specified in replacementText.
- **params:** replacementText A string that represents text to place in the Actions panel.
- **returns:** A Boolean value of true if the specified text was placed in the Actions panel; false otherwise.


## halfEdge  (6)

### `halfEdge.getEdge()`
gets the Edge object for the HalfEdge object. See Edge object.
- **params:** None. Method Description halfEdge.getEdge() Gets the Edge object for the HalfEdge object. halfEdge.getNext() Gets the next half edge on the current contour. halfEdge.getOppositeHalfEdge() Gets the HalfEdge object on the other side of the edge. halfEdge.getPrev() Gets the preceding HalfEdge object on the current contour. halfEdge.getVertex() Gets the Vertex object at the head of the HalfEdge object. Property Description halfEdge.id Read-only; a...
- **returns:** An Edge object.

### `halfEdge.getNext()`
gets the next half edge on the current contour. Note: Although half edges have a direction and a sequence order, edges do not.
- **params:** None.
- **returns:** A HalfEdge object.

### `halfEdge.getOppositeHalfEdge()`
gets the HalfEdge object on the other side of the edge.
- **params:** None.
- **returns:** A HalfEdge object.

### `halfEdge.getPrev()`
gets the preceding HalfEdge object on the current contour. Note: Although half edges have a direction and a sequence order, edges do not.
- **params:** None.
- **returns:** A HalfEdge object.

### `halfEdge.getVertex()`
gets the Vertex object at the head of the HalfEdge object. See Vertex object
- **params:** None.
- **returns:** A Vertex object

### `halfEdge.id`
a unique integer identifier for the HalfEdge object.


## matrix  (6)

### `matrix.a`
a floating-point value that specifies the (0,0) element in the transformation matrix. This value represents the scale factor of the object’s x-axis.

### `matrix.b`
a floating-point value that specifies the (0,1) element in the matrix. This value represents the vertical skew of a shape; it causes Flash to move the shape’s right edge along the vertical axis. The matrix.b and matrix.c properties in a matrix represent skewing (see matrix.c).

### `matrix.c`
a floating-point value that specifies the (1,0) element in the matrix. This value causes Flash to skew the object by moving its bottom edge along a horizontal axis. The matrix.b and matrix.c properties in a matrix represent skewing.

### `matrix.d`
a floating-point value that specifies the (1,1) element in the matrix. This value represents the scale factor of the object’s y-axis.

### `matrix.tx`
a floating-point value that specifies the x-axis location of a symbol’s registration point (also origin point or zero point) or the center of a shape. It defines the x translation of the transformation. You can move an object by setting the matrix.tx and matrix.ty properties (see matrix.ty).

### `matrix.ty`
a floating-point value that specifies the y-axis location of a symbol’s registration point or the center of a shape. It defines the y translation of the transformation. You can move an object by setting the matrix.tx and matrix.ty properties.


## presetItem  (6)

### `presetItem.isDefault`
Read-only property: a Boolean value that specifies whether the item is installed along with Flash (true) or is a custom item that you or someone else has created (false). If this value is true, you can consider it a “read-only” item; it can’t be moved, deleted, or have any similar operations appl...

### `presetItem.isFolder`
Read-only property: a Boolean value that specifies whether the item in the Motion Presets panel is a folder (true) or a preset (false).

### `presetItem.level`
Read-only property: an integer that specifies the level of the item in the folder structure of the Motion Presets panel. The Default Folder and Custom Presets folder are level 0.

### `presetItem.name`
Read-only property: a string that represents the name of the preset or folder, without path information.

### `presetItem.open`
Read-only property: specifies whether a folder in the Motion Presets panel is currently expanded (true) or not (false). This property is true if the item is not a folder. To determine if an item is a folder or a preset, use presetItem.isFolder.

### `presetItem.path`
Read-only property: a string that represents the path to the item in the Motion Presets panel folder tree, and the item name.


## RectangleObject  (5)

### `RectangleObject.bottomLeftRadius`
a float value that sets the radius of the bottom-left corner of the Rectangle object. If RectangleObject.lockFlag is true, trying to set this value has no effect. To set this value, use document.setRectangleObjectProperty(). Property Description RectangleObject.bottomLeftRadius Read-only; a float...

### `RectangleObject.bottomRightRadius`
a float value that sets the radius of the bottom-right corner of the Rectangle object. If RectangleObject.lockFlag is true, trying to set this value has no effect. To set this value, use document.setRectangleObjectProperty().

### `RectangleObject.lockFlag`
a Boolean value that determines whether different corners of the rectangle can have different radius values. If this value is true, all corners have the value assigned to RectangleObject.topLeftRadius. If it is false, each corner radius can be set independently. To set this value, use document.se...

### `RectangleObject.topLeftRadius`
a float value that sets the radius of all corners of the rectangle (if RectangleObject.lockFlag is true) or that sets only the radius of the top-left corner (if RectangleObject.lockFlag is false). To set this value, use document.setRectangleObjectProperty().

### `RectangleObject.topRightRadius`
a float value that sets the radius of the top-right corner of the Rectangle object. If RectangleObject.lockFlag is true, trying to set this value has no effect. To set this value, use document.setRectangleObjectProperty().


## bitmapInstance  (4)

### `bitmapInstance.getBits()`
lets you create bitmap effects by getting the bits out of the bitmap, manipulating them, and then returning them to Flash.
- **params:** None.
- **returns:** An object that contains width, height, depth, bits, and, if the bitmap has a color table, cTab properties. The bits element is an array of bytes. The cTab el...

### `bitmapInstance.hPixels`
an integer that represents the width of the bitmap—that is, the number of pixels in the horizontal dimension.

### `bitmapInstance.setBits(bitmap)`
sets the bits of an existing bitmap element. This lets you create bitmap effects by getting the bits out of the bitmap, manipulating them, and then returning the bitmap to Flash.
- **params:** bitmap An object that contains height, width, depth, bits, and cTab properties. The height, width, and depth propertiesare integers. The bits property is a byte array. The cTab property is required only for bitmaps with a bit depth of 8 or less and is a string that represents a color value in the form "#RRGGBB". Note: The byte array is meaningful only when referenced by an external library. You typically use it only when creating an extensible...

### `bitmapInstance.vPixels`
an integer that represents the height of the bitmap—that is, the number of pixels in the vertical dimension.


## contour  (4)

### `contour.fill`
a Fill object.

### `contour.getHalfEdge()`
returns a HalfEdge object on the contour of the selection.
- **params:** None.
- **returns:** A HalfEdge object.

### `contour.interior`
the value is true if the contour encloses an area; false otherwise.

### `contour.orientation`
an integer indicating the orientation of the contour. The value of the integer is -1 if the orientation is counterclockwise, 1 if it is clockwise, and 0 if it is a contour with no area.


## Math  (4)

### `Math.concatMatrix(mat1, mat2)`
performs a matrix concatenation and returns the result.
- **params:** mat1, mat2 Specify the Matrix objects to be concatenated (see Matrix object). Each parameter must be an object with fields a, b, c, d, tx, and ty.
- **returns:** A concatenated object matrix.

### `Math.invertMatrix(mat)`
returns the inverse of the specified matrix.
- **params:** mat Indicates the Matrix object to invert (see Matrix object). It must have the following fields: a, b, c, d, tx, and ty.
- **returns:** A Matrix object that is the inverse of the original matrix.

### `Math.pointDistance(pt1, pt2)`
computes the distance between two points.
- **params:** pt1, pt2 Specify the points between which distance is measured.
- **returns:** A floating-point value that represents the distance between the points.

### `Math.transformPoint(matrix, point)`
applies a matrix to a point.
- **params:** matrix Contains the matrix obejct applied to the point. point Contains the point to which the matrix is applied.
- **returns:** The transformed point.


## OvalObject  (4)

### `OvalObject.closePath`
a Boolean value that specifies whether the Close Path check box in the Property inspector is selected. If the start angle and end angle values for the object are the same, setting this property has no effect until the values change. To set this value, use document.setOvalObjectProperty().

### `OvalObject.endAngle`
a float value that specifies the end angle of the Oval object. Acceptable values are from 0 to 360. To set this value, use document.setOvalObjectProperty().

### `OvalObject.innerRadius`
a float value that specifies the inner radius of the Oval object as a percentage. Acceptable values are from 0 to 99. To set this value, use document.setOvalObjectProperty().

### `OvalObject.startAngle`
a float value that specifies the start angle of the Oval object. Acceptable values are from 0 to 360. To set this value, use document.setOvalObjectProperty().


## vertex  (4)

### `vertex.getHalfEdge()`
gets a HalfEdge object that shares this vertex. Method Description vertex.getHalfEdge() Gets a HalfEdge object that shares this vertex. vertex.setLocation() Sets the location of the vertex. Property Description vertex.x Read-only; the x location of the vertex in pixels. vertex.y Read-only; the y ...
- **params:** None.
- **returns:** A HalfEdge object.

### `vertex.setLocation(x, y)`
sets the location of the vertex. You must call shape.beginEdit() before using this method.
- **params:** x A floating-point value that specifies the x coordinate of where the vertex should be positioned, in pixels. y A floating-point value that specifies the y coordinate of where the vertex should be positioned, in pixels.

### `vertex.x`
the x location of the vertex, in pixels.

### `vertex.y`
the y location of the vertex, in pixels.


## outputPanel  (3)

### `outputPanel.clear()`
clears the contents of the Output panel. You can use this method in a batch processing application to clear a list of errors, or to save them incrementally by using this method with outputPanel.save().
- **params:** None.

### `outputPanel.save(fileURI [, bAppendToFile [ , bUseSystemEncoding]])`
saves the contents of the Output panel to a local text file, either by overwriting the file or by appending to the file. If fileURI is invalid or unspecified, an error is reported. This method is useful for batch processing. For example, you can create a JSFL file that compiles several components...
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the local file to contain the contents of the Output panel. bAppendToFile An optional Boolean value. If true, it appends the Output panel’s contents to the output file, and if false, the method overwrites the output file if it already exists. The default value is false. bUseSystemEncoding An optional Boolean value. If true, it saves the Output panel text using the system encoding; i...

### `outputPanel.trace(message)`
sends a text string to the Output panel, terminated by a new line, and displays the Output panel if it is not already visible. This method is identical to fl.trace(), and works in the same way as the trace() statement in ActionScript. To send a blank line, use outputPanel.trace("") or outputPanel...
- **params:** message A string that contains the text to add to the Output panel.


## compilerErrors  (2)

### `compilerErrors.clear()`
clears the contents of the Compiler Errors panel.
- **params:** None.

### `compilerErrors.save(fileURI [, bAppendToFile [, bUseSystemEncoding]])`
saves the contents of the Compiler Errors panel to a local text file.
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the filename for the saved file. If fileURI already exists, and you haven’t specified a value of true for bAppendToFile, fileURI is overwritten without warning. bAppendToFile An optional Boolean value that specifies whether the contents of the Compiler Errors panel should be appended to fileURI (true) or not (false). The default value is false. bUseSystemEncoding An optional Boolean...


## componentsPanel  (2)

### `componentsPanel.addItemToDocument(position, categoryName, componentName)`
Adds the specified component to the document at the specified position. Method Description componentsPanel.addItemToDocument() Adds the specified component to the document at the specified position. componentsPanel.reload() Refreshes the Components panel's list of components.
- **params:** position A point (for example, {x:0, y:100}) that specifies the location at which to add the component. Specify position relative to the center point of the component—not the component’s registration point (also origin point or zero point). categoryName A string that specifies the name of the component category (for example, "Data"). The valid category names are listed in the Components panel. componentName A string that specifies the name of ...

### `componentsPanel.reload()`
refreshes the Components panel’s list of components.
- **params:** None.
- **returns:** A Boolean value of true if the Component panel list is refreshed, false otherwise.


## instance  (2)

### `instance.instanceType`
a string that represents the type of instance. Possible values are "symbol", "bitmap", "embedded video", "linked video", "video", and "compiled clip". In Flash MX 2004, the value of instance.instanceType for an item added to the library using library.addNewItem("video") is "embedded_video". In Fl...

### `instance.libraryItem`
a library item used to instantiate this instance. You can change this property only to another library item of the same type (that is, you cannot set a symbol instance to refer to a bitmap). See library object.


## textRun  (2)

### `textRun.characters`
the text contained in the TextRun object.

### `textRun.textAttrs`
the TextAttrs object containing the attributes of the run of text.


## componentInstance  (1)

### `componentInstance.parameters`
an array of ActionScript 2.0 properties that are accessible from the component Property inspector. See Parameter object.

