
## symbolInstance  (30)

### `symbolInstance.accName symbolInstance.colorGreenPercent Part of the color transformation for the instance; equivalent to using the Color > Advanced setting in the instance Property inspector (the percentage controls on the left of the dialog box). symbolInstance.colorMode A string that specifies the color mode as identified in the symbol Property inspector Color pop-up menu. symbolInstance.co`
a string that is equivalent to the Name field in the Accessibility panel. Screen readers identify objects by reading the name aloud. This property is not available for graphic symbols.

### `symbolInstance.backgroundColor`
a string that specifies the matte color when 24 bit mode is selected for the instance. This is a string in hexadecimal #rrggbb format or an integer containing the value.

### `symbolInstance.bitmapRenderMode`
a string that sets the display type for the symbol. Acceptable values include:  “none”  “cache” - sets the symbol to be cached as a bitmap by Flash Player at runtime.  “export” - sets the symbol to be exported as a bitmap when the SWF is compiled. The older “symbolInstance.cacheAsBitmap” on pa...

### `symbolInstance.blendMode`
a string that specifies the blending mode to be applied to a movie clip symbol. Acceptable values are "normal", "layer", "multiply", "screen", "overlay", "hardlight", "lighten", "darken", "difference", "add", "subtract", "invert", "alpha", and "erase".

### `symbolInstance.brightness`
returns the value set in the color effect Property Inspector for brightness (percentage between - 100 and 100) when colorMode == 'brightness';. Error if colorMode is a different setting.

### `symbolInstance.buttonTracking`
a string that, for button symbols only, sets the same property as the pop-up menu for Track As Button or Track As Menu Item in the Property inspector. For other types of symbols, this property is ignored. Acceptable values are "button" or "menu".

### `symbolInstance.cacheAsBitmap`
a Boolean value that specifies whether run-time bitmap caching is enabled. Note: Starting w/ Flash Professional CS5.5, users should switch to using the “symbolInstance.bitmapRenderMode” on page 470 property instead of this property.

### `symbolInstance.colorAlphaAmount`
an integer that is part of the color transformation for the instance, specifying the Advanced Effect Alpha settings. This property is equivalent to using the Color > Advanced setting in the Property inspector and adjusting the controls on the right of the dialog box. This value either reduces or ...

### `symbolInstance.colorAlphaPercent`
an integer that specifies part of the color transformation for the instance. This property is equivalent to using the Color > Advanced setting in the instance Property inspector (the percentage controls on the left of the dialog box). This value changes the tint and alpha values to a specified pe...

### `symbolInstance.colorBlueAmount`
an integer that is part of the color transformation for the instance. This property is equivalent to using the Color > Advanced setting in the instance Property inspector. Allowable values are from -255 to 255.

### `symbolInstance.colorBluePercent`
an integer that is part of the color transformation for the instance. This property is equivalent to using the Color > Advanced setting in the instance Property inspector (the percentage controls on the left of the dialog box). This value sets the blue values to a specified percentage. Allowable ...

### `symbolInstance.colorGreenAmount`
an integer that is part of the color transformation for the instance. This property is equivalent to using the Color > Advanced setting in the instance Property inspector. Allowable values are from -255 to 255.

### `symbolInstance.colorGreenPercent`
part of the color transformation for the instance. This property is equivalent to using the Color > Advanced setting in the instance Property inspector (the percentage controls on the left of the dialog box). This value sets the green values by a specified percentage. Allowable values are from -1...

### `symbolInstance.colorMode`
a string that specifies the color mode as identified in the symbol Property inspector Color pop-up menu. Acceptable values are "none", "brightness", "tint", "alpha", and "advanced".

### `symbolInstance.colorRedAmount`
an integer that is part of the color transformation for the instance. This property is equivalent to using the Color > Advanced setting in the instance Property inspector. Allowable values are from -255 to 255.

### `symbolInstance.colorRedPercent`
part of the color transformation for the instance. This property is equivalent to using the Color > Advanced setting in the instance Property inspector (the percentage controls on the left of the dialog box). This value sets the red values to a specified percentage. Allowable values are from -100...

### `symbolInstance.description`
a string that is equivalent to the Description field in the Accessibility panel. The description is read by the screen reader. This property is not available for graphic symbols.

### `symbolInstance.filters`
an array of Filter objects (see Filter object). To modify filter properties, you don’t write to this array directly. Instead, retrieve the array, set the individual properties, and then set the array to reflect the new properties.

### `symbolInstance.firstFrame`
a zero-based integer that specifies the first frame to appear in the timeline of the graphic. This property applies only to graphic symbols and sets the same property as the First field in the Property inspector. For other types of symbols, this property is undefined.

### `symbolInstance.forceSimple`
a Boolean value that enables and disables the accessibility of the object’s children. This property is equivalent to the inverse logic of the Make Child Objects Accessible setting in the Accessibility panel. For example, if forceSimple is true, it is the same as the Make Child Object Accessible o...

### `symbolInstance.is3D`
a boolean value that indicates whether the symbol instance contains a 3D matrix (transform).

### `symbolInstance.loop`
a string that, for graphic symbols, sets the same property as the Loop pop-up menu in the Property inspector. For other types of symbols, this property is undefined. Acceptable values are "loop", "play once", and "single frame" to set the graphic’s animation accordingly.

### `symbolInstance.shortcut`
a string that is equivalent to the shortcut key associated with the symbol. This property is equivalent to the Shortcut field in the Accessibility panel. This key is read by the screen readers. This property is not available for graphic symbols.

### `symbolInstance.silent`
a Boolean value that enables or disables the accessibility of the object. This property is equivalent to the inverse logic of the Make Object Accessible setting in the Accessibility panel. For example, if silent is true, it is the same as the Make Object Accessible option being unchecked. If sile...

### `symbolInstance.symbolType`
a string that specifies the type of symbol. This property is equivalent to the value for Behavior in the Create New Symbol and Convert To Symbol dialog boxes. Acceptable values are "button", "movie clip", and "graphic".

### `symbolInstance.tabIndex`
an integer that is equivalent to the Tab index field in the Accessibility panel. Creates a tab order in which objects are accessed when the user presses the Tab key. This property is not available for graphic symbols.

### `symbolInstance.tintColor`
when the Color Effect Property Inspector is using style tint (colorMode == 'tint'), return the color applied to the tint. Otherwise using this property results in an error.

### `symbolInstance.tintPercent`
when the Color Effect Property Inspector is using style tint (colorMode == 'tint'), then return the tint percentage from -100 to 100. Otherwise using this property results in an error.

### `symbolInstance.useBackgroundColor`
a boolean value that indicates whether to use 24 bit mode (true) or 32 bit mode with alpha (false) for the instance. If true, the backgroundColor specified for the instance is used.

### `symbolInstance.visible`
a boolean value that sets the Visible property of an object to on (true) or off (false).

