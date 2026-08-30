
## stroke  (25)

### `stroke.breakAtCorners`
a Boolean value. This property is the same as the Sharp Corners setting in the custom Stroke Style dialog box.

### `stroke.capType`
a string that specifies the type of cap for the stroke. Acceptable values are "none", "round", and "square".

### `stroke.color`
the color of the stroke, in one of the following formats:  A string in the format "#RRGGBB" or "#RRGGBBAA"  A hexadecimal number in the format 0xRRGGBB  An integer that represents the decimal equivalent of a hexadecimal number

### `stroke.curve`
a string that specifies the type of hatching for the stroke. This property can be set only if the stroke.style property is set to "hatched" (see stroke.style). Acceptable values are "straight", "slight curve", "medium curve", and "very curved".

### `stroke.dash1`
an integer that specifies the lengths of the solid parts of a dashed line. This property is available only if the stroke.style property is set to dashed(see stroke.style).

### `stroke.dash2`
an integer that specifies the lengths of the blank parts of a dashed line. This property is available only if the stroke.style property is set to dashed (see stroke.style).

### `stroke.density`
a string that specifies the density of a stippled line. This property is available only if the stroke.style property is set to stipple (see stroke.style). Acceptable values are "very dense", "dense", "sparse", and "very sparse".

### `stroke.dotSize`
a string that specifies the dot size of a stippled line. This property is available only if the stroke.style property is set to stipple (see stroke.style). Acceptable values are "tiny", "small", "medium", and "large". The following example sets the dotSize property to tiny for the stroke style of...

### `stroke.dotSpace`
an integer that specifies the spacing between dots in a dotted line. This property is available only if the stroke.style property is set to dotted. See stroke.style.

### `stroke.hatchThickness`
a string that specifies the thickness of a hatch line. This property is available only if the stroke.style property is set to hatched (see stroke.style). Acceptable values are "hairline", "thin", "medium", and "thick".

### `stroke.jiggle`
a string that specifies the jiggle property of a hatched line. This property is available only if the stroke.style property is set to hatched (see stroke.style). Acceptable values are "none", "bounce", "loose", and "wild".

### `stroke.joinType`
a string that specifies the type of join for the stroke. Acceptable values are "miter", "round", and "bevel".

### `stroke.length`
a string that specifies the length of a hatch line. This property is available only if the stroke.style property is set to hatched (see stroke.style). Acceptable values are "equal", "slight variation", "medium variation", and "random". (The value "random" actually maps to "medium variation".)

### `stroke.miterLimit`
a float value that specifies the angle above which the tip of the miter will be truncated by a segment. That means the miter is truncated only if the miter angle is greater than the value of miterLimit.

### `stroke.pattern`
a string that specifies the pattern of a ragged line. This property is available only if the stroke.style property is set to ragged (see stroke.style). Acceptable values are "solid", "simple", "random", "dotted", "random dotted", "triple dotted", and "random triple dotted".

### `stroke.rotate`
a string that specifies the rotation of a hatch line. This property is available only if the stroke.style property is set to hatched (see stroke.style). Acceptable values are "none", "slight", "medium", and "free".

### `stroke.scaleType`
a string that specifies the type of scale to be applied to the stroke. Acceptable values are "normal", "horizontal", "vertical", and "none".

### `stroke.shapeFill`
a Fill object that represents the fill settings of the stroke.

### `stroke.space`
a string that specifies the spacing of a hatched line. This property is available only if the stroke.style property is set to hatched (see stroke.style). Acceptable values are "very close", "close", "distant", and "very distant".

### `stroke.strokeHinting`
a Boolean value that specifies whether stroke hinting is set on the stroke.

### `stroke.style`
a string that describes the stroke style. Acceptable values are "noStroke","solid", "dashed", "dotted", "ragged", "stipple", and "hatched". Some of these values require additional properties of the Stroke object to be set, as described in the following list:  If value is "solid" or "noStroke", t...

### `stroke.thickness`
an integer that specifies the stroke size.

### `stroke.variation`
a string that specifies the variation of a stippled line. This property is available only if the stroke.style property is set to stipple (see stroke.style). Acceptable values are "one size", "small variation", "varied sizes", and "random sizes".

### `stroke.waveHeight`
a string that specifies the wave height of a ragged line. This property is available only if the stroke.style property is set to ragged (see stroke.style). Acceptable values are "flat", "wavy", "very wavy", and "wild".

### `stroke.waveLength`
a string that specifies the wavelength of a ragged line. This property is available only if the stroke.style property is set to ragged (see stroke.style). Acceptable values are "very short", "short", "medium", and "long".

