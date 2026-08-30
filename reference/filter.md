
## filter  (19)

### `filter.angle`
a float value that specifies the angle of the shadow or highlight color, in degrees. Acceptable values are between 0 and 360. This property is defined for Filter objects with a value of "bevelFilter", "dropShadowFilter", "gradientBevelFilter", or "gradientGlowFilter" for the filter.name property.

### `filter.blurX`
a float value that specifies the amount to blur in the x direction, in pixels. Acceptable values are between 0 and 255. This property is defined for Filter objects with a value of "bevelFilter", "blurFilter", "dropShadowFilter", "glowFilter", "gradientBevelFilter", or "gradientGlowFilter" for the...

### `filter.blurY`
a float value that specifies the amount to blur in the y direction, in pixels. Acceptable values are between 0 and 255. This property is defined for Filter objects with a value of "bevelFilter", "blurFilter", "dropShadowFilter", "glowFilter", "gradientBevelFilter", or "gradientGlowFilter" for the...

### `filter.brightness`
a float value that specifies the brightness of the filter. Acceptable values are between -100 and 100. This property is defined for Filter objects with a value of "adjustColorFilter" for the filter.name property.

### `filter.color`
the color of the filter, in one of the following formats:  A string in the format "#RRGGBB" or "#RRGGBBAA"  A hexadecimal number in the format 0xRRGGBB  An integer that represents the decimal equivalent of a hexadecimal number This property is defined for Filter objects with a value of "dropSh...

### `filter.contrast`
a float value that specifies the contrast value of the filter. Acceptable values are between -100 and 100. This property is defined for Filter objects with a value of "adjustColorFilter" for the filter.name property.

### `filter.distance`
a float value that specifies the distance between the filter’s effect and an object, in pixels. Acceptable values are from -255 to 255. This property is defined for Filter objects with a value of "bevelFilter", "dropShadowFilter", "gradientBevelFilter", or "gradientGlowFilter" for the filter.name...

### `filter.enabled`
a Boolean value that specifies whether the specified filter is enabled (true) or disabled (false).

### `filter.hideObject`
a Boolean value that specifies whether the source image is hidden (true) or displayed (false). This property is defined for Filter objects with a value of "dropShadowFilter" for the filter.name property.

### `filter.highlightColor`
the color of the highlight, in one of the following formats:  A string in the format "#RRGGBB" or "#RRGGBBAA"  A hexadecimal number in the format 0xRRGGBB  An integer that represents the decimal equivalent of a hexadecimal number This property is defined for Filter objects with a value of "bev...

### `filter.hue`
a float value that specifies the hue of the filter. Acceptable values are between -180 and 180. This property is defined for Filter objects with a value of "adjustColorFilter" for the filter.name property.

### `filter.inner`
a Boolean value that specifies whether the shadow is an inner shadow (true) or not (false). This property is defined for Filter objects with a value of "dropShadowFilter" or "glowFilter" for the filter.name property.

### `filter.knockout`
a Boolean value that specifies whether the filter is a knockout filter (true) or not (false). This property is defined for Filter objects with a value of "bevelFilter", "dropShadowFilter", "glowFilter", "gradientBevelFilter", or "gradientGlowFilter" for the filter.name property.

### `filter.name`
a string that specifies the type of filter. The value of this property determines which other properties of the Filter object are available. The value is one of the following: "adjustColorFilter", "bevelFilter", "blurFilter", "dropShadowFilter", "glowFilter", "gradientBevelFilter", or "gradientGl...

### `filter.quality`
a string that specifies the blur quality. Acceptable values are "low", "medium", and "high" ("high" is similar to a Gaussian blur). This property is defined for Filter objects with a value of "bevelFilter", "blurFilter", "dropShadowFilter", "glowFilter", "gradientGlowFilter", or "gradientBevelFil...

### `filter.saturation`
a float value that specifies the saturation value of the filter. Acceptable values are from -100 to 100. This property is defined for Filter objects with a value of "adjustColorFilter" for the filter.name property.

### `filter.shadowColor`
the color of the shadow, in one of the following formats:  A string in the format "#RRGGBB" or "#RRGGBBAA"  A hexadecimal number in the format 0xRRGGBB  An integer that represents the decimal equivalent of a hexadecimal number This property is defined for Filter objects with a value of "bevelF...

### `filter.strength`
an integer that specifies the percentage strength of the filter. Acceptable values are between 0 and 25,500. This property is defined for Filter objects with a value of "bevelFilter", "dropShadowFilter", "glowFilter", "gradientGlowFilter", or "gradientBevelFilter" for the filter.name property.

### `filter.type`
a string that specifies the type of bevel or glow. Acceptable values are "inner", "outer", and "full". This property is defined for Filter objects with a value of "bevelFilter", "gradientGlowFilter", or "gradientBevelFilter" for the filter.name property.

