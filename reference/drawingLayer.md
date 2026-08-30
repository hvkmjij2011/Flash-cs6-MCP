
## drawingLayer  (11)

### `drawingLayer.beginDraw([persistentDraw]) Method Description drawingLayer.beginDraw() Puts Flash in drawing mode. drawingLayer.beginFrame() Erases what was previously drawn using the drawingLayer and prepares for more drawing commands. drawingLayer.cubicCurveTo() Draws a cubic curve from the current pen location using the parameters as the coordinates of the cubic segment. drawingLayer.curveTo`
puts Flash in drawing mode. Drawing mode is used for temporary drawing while the mouse button is pressed. You typically use this method only when creating extensible tools.
- **params:** persistentDraw A Boolean value (optional). If set to true, it indicates that the drawing in the last frame remains on the Stage until a new beginDraw() or beginFrame() call is made. (In this context, frame refers to where you start and end drawing; it does not refer to timeline frames.) For example, when users draw a rectangle, they can preview the outline of the shape while dragging the mouse. If you want that preview shape to remain after th...

### `drawingLayer.beginFrame()`
erases what was previously drawn using the drawingLayer and prepares for more drawing commands. Should be called after drawingLayer.beginDraw(). Everything drawn between drawingLayer.beginFrame() and an drawingLayer.endFrame() remains on the Stage until you call the next beginFrame() and endFrame...
- **params:** None.

### `drawingLayer.cubicCurveTo(x1Ctrl, y1Ctrl, x2Ctl, y2Ctl, xEnd, yEnd)`
draws a cubic curve from the current pen location using the parameters as the coordinates of the cubic segment. You typically use this method only when creating extensible tools.
- **params:** x1Ctl A floating-point value that is the x location of the first control point. y1Ctl A floating-point value that is the y location of the first control point. x2Ctl A floating-point value that is the x position of the middle control point. y2Ctl A floating-point value that is the y position of the middle control point. xEnd A floating-point value that is the x position of the end control point. yEnd A floating-point value that is the y positi...

### `drawingLayer.curveTo(xCtl, yCtl, xEnd, yEnd)`
draws a quadratic curve segment starting at the current drawing position and ending at a specified point. You typically use this method only when creating extensible tools.
- **params:** xCtl A floating-point value that is the x position of the control point. yCtl A floating-point value that is the y position of the control point. xEnd A floating-point value that is the x position of the end control point. yEnd A floating-point value that is the y position of the end control point.

### `drawingLayer.drawPath(path)`
draws the path specified by the path parameter. You typically use this method only when creating extensible tools.
- **params:** path A Path object to draw.

### `drawingLayer.endDraw()`
exits drawing mode. Drawing mode is used when you want to temporarily draw while the mouse button is pressed. You typically use this method only when creating extensible tools.
- **params:** None.

### `drawingLayer.endFrame()`
signals the end of a group of drawing commands. A group of drawing commands refers to everything drawn between drawingLayer.beginFrame() and drawingLayer.endFrame(). The next call to drawingLayer.beginFrame() will erase whatever was drawn in this group of drawing commands. You typically use this ...
- **params:** None.

### `drawingLayer.lineTo(x, y)`
draws a line from the current drawing position to the point (x,y). You typically use this method only when creating extensible tools.
- **params:** x A floating-point value that is the x coordinate of the end point of the line to draw. y A floating-point value that is the y coordinate of the end point of the line to draw.

### `drawingLayer.moveTo(x, y)`
sets the current drawing position. You typically use this method only when creating extensible tools.
- **params:** x A floating-point value that specifies the x coordinate of the position at which to start drawing. y A floating-point value that specifies the y coordinate of the position at which to start drawing.

### `drawingLayer.newPath()`
returns a new Path object. You typically use this method only when creating extensible tools. See Path object.
- **params:** None.
- **returns:** A Path object.

### `drawingLayer.setColor(color)`
sets the color of subsequently drawn data. Applies only to persistent data. To use this method, the parameter passed to drawingLayer.beginDraw() must be set to true. You typically use this method only when creating extensible tools. See drawingLayer.beginDraw().
- **params:** color The color of subsequently drawn data, in one of the following formats:  A string in the format "#RRGGBB" or "#RRGGBBAA"  A hexadecimal number in the format 0xRRGGBB  An integer that represents the decimal equivalent of a hexadecimal number

