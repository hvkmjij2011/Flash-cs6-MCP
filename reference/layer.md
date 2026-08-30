
## layer  (11)

### `layer.animationType Property Description layer.animationTyp e The layer type: "none", "motion object", or "IK pose". layer.color A string, hexadecimal value, or integer that specifies the color assigned to outline the layer. layer.frameCount Read-only; an integer that specifies the number of frames in the layer. layer.frames Read-only; an array of Frame objects. layer.height An integer that speci`
a string value indicating the animation type of the layer. Possible values include: "none", "motion object", "IK pose".

### `layer.color`
the color assigned to outline the layer, in one of the following formats:  A string in the format "#RRGGBB" or "#RRGGBBAA"  A hexadecimal number in the format 0xRRGGBB  An integer that represents the decimal equivalent of a hexadecimal number This property is equivalent to the Outline color se...

### `layer.frameCount`
an integer that specifies the number of frames in the layer.

### `layer.frames`
an array of Frame objects (see Frame object).

### `layer.height`
an integer that specifies the percentage layer height; equivalent to the Layer height value in the Layer Properties dialog box. Acceptable values represent percentages of the default height: 100, 200, or 300.

### `layer.layerType`
a string that specifies the current use of the layer; equivalent to the Type setting in the Layer Properties dialog box. Acceptable values are "normal", "guide", "guided", "mask", "masked", and "folder".

### `layer.locked`
a Boolean value that specifies the locked status of the layer. If set to true, the layer is locked. The default value is false.

### `layer.name`
a string that specifies the name of the layer.

### `layer.outline`
a Boolean value that specifies the status of outlines for all objects in the layer. If set to true, all objects in the layer appear only with outlines. If false, objects appear as they were created.

### `layer.parentLayer`
a Layer object that represents the layer’s containing folder, guiding, or masking layer. The parent layer must be a folder, guide, or mask layer that precedes the layer, or the parentLayer of the preceding or following layer. Setting the layer’s parentLayer does not move the layer’s position in t...

### `layer.visible`
a Boolean value that specifies whether the layer’s objects on the Stage are shown or hidden. If set to true, all objects in the layer are visible; if false, they are hidden. The default value is true.

