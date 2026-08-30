
## shape  (14)

### `shape.beginEdit()`
defines the start of an edit session. You must use this method before issuing any commands that change the Shape object or any of its subordinate parts.
- **params:** None.

### `shape.contours`
an array of Contour objects for the shape (see Contour object).

### `shape.deleteEdge(index)`
deletes the specified edge. You must call shape.beginEdit() before using this method.
- **params:** index A zero-based index that specifies the edge to delete from the shape.edges array. This method changes the length of the shape.edges array.

### `shape.edges`
an array of Edge objects (see Edge object).

### `shape.endEdit()`
defines the end of an edit session for the shape. All changes made to the Shape object or any of its subordinate parts will be applied to the shape. You must use this method after issuing any commands that change the Shape object or any of its subordinate parts.
- **params:** None.

### `shape.getCubicSegmentPoints(cubicSegmentIndex)`
returns an array of points that define a cubic curve.
- **params:** cubicSegmentIndex An integer that specifies the cubic segment for which points are returned.
- **returns:** An array of points that define a cubic curve for the Edge object that corresponds to the specified cubicSegmentIndex (see edge.cubicSegmentIndex).

### `shape.isDrawingObject`
if true, the shape is a drawing object.

### `shape.isFloating`
if true, the shape is floating above the parent frame’s (or group’s) shape. Also, if true, this type of shape will have it's own matrix, similar to a drawing object.

### `shape.isGroup`
if true, the shape is a group. A group can contain different types of elements, such as text elements and symbols. However, the group itself is considered a shape, and you can use the shape.isGroup property no matter what types of elements the group contains.

### `shape.isOvalObject`
if true, the shape is a primitive Oval object (was created using the Oval Primitive tool).

### `shape.isRectangleObject`
if true, the shape is a primitive Rectangle object (was created using the Rectangle Primitive tool).

### `shape.members`
an array of objects in the currently selected group. This property is available only if the value of shape.isGroup is true). Raw shapes in the group are not included in the shape.members array. For example, if the group contains three drawing objects and three raw shapes, the shape.members array ...

### `shape.numCubicSegments`
the number of cubic segments in the shape.

### `shape.vertices`
an array of Vertex objects (see Vertex object).

