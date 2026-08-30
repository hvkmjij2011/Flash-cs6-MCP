
## tools  (12)

### `tools.activeTool`
returns the ToolObj object for the currently active tool.

### `tools.altIsDown`
a Boolean value that identifies if the Alt key is being pressed. The value is true if the Alt key is pressed, and false otherwise.

### `tools.constrainPoint(pt1, pt2)`
takes two points and returns a new adjusted or constrained point. If the Shift key is pressed when the command is run, the returned point is constrained to follow either a 45º constrain (useful for something such as a line with an arrowhead) or to constrain an object to maintain its aspect ratio ...
- **params:** pt1, pt2 Points that specify the starting-click point and the drag-to point.
- **returns:** A new adjusted or constrained point.

### `tools.ctlIsDown`
a Boolean value that is true if the Control key is pressed; false otherwise.

### `tools.getKeyDown()`
returns the most recently pressed key.
- **params:** None.
- **returns:** The integer value of the key.

### `tools.mouseIsDown`
a Boolean value that is true if the left mouse button is currently down; false otherwise.

### `tools.penDownLoc`
a point that represents the position of the last mouse-down event on the Stage. The tools.penDownLoc property comprises two properties, x and y, corresponding to the x,y location of the mouse pointer.

### `tools.penLoc`
a point that represents the current location of the mouse pointer. The tools.penLoc property comprises two properties, x and y, corresponding to the x,y location of the mouse pointer.

### `tools.setCursor(cursor)`
sets the pointer to a specified appearance.
- **params:** cursor An integer that defines the pointer appearance, as described in the following list:  0 = Plus cursor (+)  1 = black arrow  2 = white arrow  3 = four-way arrow  4 = two-way horizontal arrow  5 = two-way vertical arrow  6 = X  7 = hand cursor

### `tools.shiftIsDown`
a Boolean value that is true if the Shift key is pressed; false otherwise.

### `tools.snapPoint(pt)`
takes a point as input and returns a new point that may be adjusted or snapped to the nearest geometric object. If snapping is disabled in the View menu in the Flash user interface, the point returned is the original point.
- **params:** pt Specifies the location of the point for which you want to return a snap point.
- **returns:** A new point that may be adjusted or snapped to the nearest geometric object.

### `tools.toolObjs`
an array of ToolObj objects (see ToolObj object). 570 Chapter 49: Tween Object Tween object Summary
- **params:** frameIndex Offset index of interpolated frame.
- **returns:** Value object {"colorAlphaAmount", "colorAlphaPercent", "colorRedAmount", "colorRedPercent", "colorGreenAmount", "colorGreenPercent", "colorBlueAmount", "colo...

