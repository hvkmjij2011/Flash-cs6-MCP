
## compiledClipInstance  (24)

### `compiledClipInstance.accName`
a string that is equivalent to the Name field in the Accessibility panel. Screen readers identify objects by reading the name aloud.

### `compiledClipInstance.backgroundColor`
a string that specifies the matte color when Opaque is selected. This is a string in hexadecimal #rrggbb format or an integer containg the value.

### `compiledClipInstance.blendMode`
a string that specifies the blend mode. Valid blend modes are: normal, layer, darken, multiply, lighten, screen, overlay, hardlight, add, subtract, difference, invert, alpha, and erase.

### `compiledClipInstance.brightness`
an int that contains the value set in the Color Effect Property Inspector for brightness when colorMode == 'brightness'. Specify a percentage between -100 and 100. Returns an error if colorMode is a different setting.

### `compiledClipInstance.cacheAsBitmap`
a boolean that indicates whether to cache bitmaps. (Equivalent to Use runtime bitmap caching in the Property Inspector). The default is false.

### `compiledClipInstance.colorAlphaAmount`
an int that reduces or increases the tint and alpha values by a constant amount. This value is added to the current value. This setting is most useful if used in conjunction with colorAlphaPercent. Valid values are -255 to 255. This setting is the same as selecting Color > Advanced in the Instanc...

### `compiledClipInstance.colorAlphaPercent`
an int that reduces or increases the tint and alpha values by a specified percentage. The current values are multiplied by this percentage. Valid values are -100 to 100. This setting is the same as selecting Color > Advanced in the Instance Property Inspector and adjusting the controls on the lef...

### `compiledClipInstance.colorBlueAmount`
an int that either reduces or increases the blue tint by a constant amount. This value is added to the current value. Valid values are -255 to 255. This setting is the same as selecting Color > Advanced in the Instance Property Inspector.

### `compiledClipInstance.colorBluePercent`
an int that reduces or increases the blue tint values by a specified percentage. The current values are multiplied by this percentage. Valid values are -100 to 100. This setting is the same as selecting Color > Advanced in the Instance Property Inspector.

### `compiledClipInstance.colorGreenAmount`
an int that either reduces or increases the green tint by a constant amount. This value is added to the current value. Valid values are -255 to 255. This setting is the same as selecting Color > Advanced in the Instance Property Inspector.

### `compiledClipInstance.colorGreenPercent`
an int that reduces or increases the green tint values by a specified percentage. The current values are multiplied by this percentage. Valid values are -100 to 100. This setting is the same as selecting Color > Advanced in the Instance Property Inspector.

### `compiledClipInstance.colorMode`
a string that specifies the color mode, as identified in the Symbol Properties dialog. Valid values are “none”, “brightness”, “tint”, “alpha”, and “advanced”.

### `compiledClipInstance.colorRedAmount`
an int that either reduces or increases the red tint by a constant amount. This value is added to the current value. Valid values are -255 to 255. This setting is the same as selecting Color > Advanced in the Instance Property Inspector.

### `compiledClipInstance.colorRedPercent`
an int that reduces or increases the red tint values by a specified percentage. The current values are multiplied by this percentage. Valid values are -100 to 100. This setting is the same as selecting Color > Advanced in the Instance Property Inspector.

### `compiledClipInstance.description`
a string that is equivalent to the Description field in the Accessibility panel. The description is read by the screen reader.

### `compiledClipInstance.filters`
an array of Filter objects. The properties of Filter object in the filters array can be read but cannot be written directly by accessing the filters array. To set the properties of the filter objects in the filters array, first retrieve the array, set the properties, set it back to the filters ar...

### `compiledClipInstance.forceSimple`
a Boolean value that enables and disables the children of the object to be accessible. This is equivalent to the inverse logic of the Make Child Objects Accessible setting in the Accessibility panel. If forceSimple is true, it is the same as the Make Child Objects Accessible option being unchecke...

### `compiledClipInstance.shortcut`
a string that is equivalent to the Shortcut field in the Accessibility panel. The shortcut is read by the screen reader. This property is not available for dynamic text fields.

### `compiledClipInstance.silent`
a Boolean value that enables or disables the accessibility of the object; equivalent to the inverse logic of Make Object Accessible setting in the Accessibility panel. That is, if silent is true, then Make Object Accessible is unchecked. If silent is false, then Make Object Accessible is checked.

### `compiledClipInstance.tabIndex`
an integer that is equivalent to the Tab Index field in the Accessibility panel. Creates a tab order in which objects are accessed when the user presses the Tab key.

### `compiledClipInstance.tintColor`
a Color object that, when the Color Effect Property Inspector is using style tint (colorMode == 'tint'), returns the color applied to the tint. Otherwise, using this property results in an error.

### `compiledClipInstance.tintPercent`
a string that, when the Color Effect Property Inspector is using style tint (colorMode == 'tint'), returns the tint percentage from -100 to 100. Otherwise, using this property results in an error.

### `compiledClipInstance.useBackgroundColor`
a boolean that sets the background color:  true - Use 32-bit with alpha.  false - Use the background color.

### `compiledClipInstance.visible`
a boolean that sets visibility. Equivalent to the visible checkbox in the Display section of the Property Inspector for symbols.

