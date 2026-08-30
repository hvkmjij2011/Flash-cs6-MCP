
## element  (28)

### `element.depth`
an integer that has a value greater than 0 for the depth of the object in the view. The drawing order of objects on the Stage specifies which one is on top of the others. Object order can also be managed with the Modify > Arrange menu item.

### `element.elementType`
a string that represents the type of the specified element. The value is one of the following:  "shape"  "text"  "tlfText" (Flash Pro CS5 and later)  "instance"  "shapeObj"

### `element.getPersistentData(name)`
retrieves the value of the data specified by the name parameter. The type of data depends on the type of the data that was stored (see element.setPersistentData()). Only symbols and bitmaps support persistent data.
- **params:** name A string that identifies the data to be returned.
- **returns:** The data specified by the name parameter, or 0 if the data doesn’t exist.

### `element.getPublishPersistentData(name, format)`
Indicates whether publishing of a specified persistent data item is enabled for the specified format on an element.
- **params:** name A string that specifies the name of the persistent data item (set with element.setPersistentData()). format A string that specifies the publishing format. Note: _EMBED_SWF_ is a special built-in publishing format for persistent data. If set, the persistent data will be embedded in the SWF file every time a document is published. The persistent data can then be accessed via ActionScript with the .metaData property. This requires SWF versio...
- **returns:** Boolean; True if the specified persistent data is enabled for the specified format. Otherwise False.

### `element.getTransformationPoint()`
gets the value of the specified element’s transformation point. Transformation points are relative to different locations, depending on the type of item selected. For more information, see element.setTransformationPoint().
- **params:** None.
- **returns:** A point (for example, {x:10, y:20}, where x and y are floating-point numbers) that specifies the position of the transformation point (also origin point or z...

### `element.hasPersistentData(name)`
determines whether the specified data has been attached to the specified element. Only symbols and bitmaps support persistent data.
- **params:** name A string that specifies the name of the data item to test.
- **returns:** A Boolean value: true if the specified data is attached to the object; false otherwise.

### `element.height`
a float value that specifies the height of the element in pixels. Do not use this property to resize a text field. Instead, select the text field and use document.setTextRectangle(). Using this property with a text field scales the text.

### `element.layer`
represents the Layer object on which the element is located.

### `element.left`
a float value that represents the left side of the element. The value of element.left is relative to the upper left of the Stage for elements that are in a scene and is relative to the symbol’s registration point (also origin point or zero point) if the element is stored within a symbol. Use docu...

### `element.locked`
a Boolean value: true if the element is locked; false otherwise. If the value of element.elementType is "shape", this property is ignored.

### `element.matrix`
a Matrix object. A matrix has properties a, b, c, d, tx, and ty. The a, b, c, and d properties are floating-point values; the tx and ty properties are coordinates. See Matrix object.

### `element.name`
a string that specifies the name of the element, normally referred to as the Instance name. If the value of element.elementType is "shape", this property is ignored. See element.elementType.

### `element.removePersistentData(name)`
removes any persistent data with the specified name that has been attached to the object. Only symbols and bitmaps support persistent data.
- **params:** name A string that specifies the name of the data to remove.
- **returns:** A Boolean value: true if data was removed; false otherwise.

### `element.rotation`
an integer or float value between -180 and 180 that specifies the object’s clockwise rotation, in degrees.

### `element.scaleX`
a float value that specifies the x scale value of symbols, drawing objects, and primitive rectangles and ovals. A value of 1 indicates 100 percent scale.

### `element.scaleY`
a float value that specifies the y scale value of symbols, drawing objects, and primitive rectangles and ovals. A value of 1 indicates 100 percent scale.

### `element.selected`
a Boolean value that specifies whether the element is selected (true) or not (false).

### `element.setPersistentData(name, type, value)`
stores data with an element. The data is available when the FLA file containing the element is reopened. Only symbols and bitmaps support persistent data.
- **params:** name A string that specifies the name to associate with the data. This name is used to retrieve the data. type A string that defines the type of the data. The allowable values are "integer", "integerArray", "double", "doubleArray", "string", and "byteArray". value Specifies the value to associate with the object. The data type of value depends on the value of the type parameter. The specified value should be appropriate to the data type specif...

### `element.setPublishPersistentData(name, format, publish)`
Enables or disables publishing of persistent data for a specified format.
- **params:** name A string that specifies the name of the persistent data item (set with element.setPersistentData()). format A string that specifies the publishing format. Note: _EMBED_SWF_ is a special built-in publishing format for persistent data. If set, the persistent data will be embedded in the SWF file every time a document is published. The persistent data can then be accessed via ActionScript with the .metaData property. This requires SWF versio...
- **returns:** None.

### `element.setTransformationPoint(transformationPoint)`
sets the position of the element’s transformation point. This method is almost identical to document.setTransformationPoint(). It is different in the following way:  You can set transformation points for elements without first selecting them. This method moves the transformation point but does n...
- **params:** transformationPoint A point (for example, {x:10, y:20}, where x and y are floating-point numbers) that specifies values for an element’s or group’s transformation point.  Shapes: transformationPoint is set relative to the document (0,0 is the upper-left corner of the Stage).  Symbols: transformationPoint is set relative to the symbol’s registration point (0,0 is located at the registration point).  Text: transformationPoint is set relative ...

### `element.skewX`
a float value between -180 and 180 that specifies the x skew value of symbols, drawing objects, and primitive rectangles and ovals.

### `element.skewY`
a float value between -180 and 180 that specifies the y skew value of symbols, drawing objects, and primitive rectangles and ovals.

### `element.top`
top side of the element. The value of element.top is relative to the upper left of the Stage for elements that are in a scene and is relative to the symbol’s registration point if the element is stored within a symbol. Use document.setSelectionBounds() or document.moveSelectionBy() to set this pr...

### `element.transformX`
a floating-point number that specifies the x value of the selected element’s transformation point, within the coordinate system of the element's parent. Setting this property to a new value moves the element. By contrast, the element.setTransformationPoint() method moves the transformation point ...

### `element.transformY`
a floating-point number that specifies the y value of the selected element’s transformation point, within the coordinate system of the element’s parent. Setting this property to a new value moves the element. By contrast, the element.setTransformationPoint() method moves the transformation point ...

### `element.width`
a float value that specifies the width of the element in pixels. Do not use this property to resize a text field. Instead, select the text field and use document.setTextRectangle(). Using this property with a text field scales the text.

### `element.x`
a float value that specifies the x value of the selected element’s registration point.

### `element.y`
a float value that specifies the y value of the selected element’s registration point.

