
## frame  (41)

### `frame.actionScript`
a string that represents ActionScript code. To insert a new line character, use "\n".

### `frame.convertMotionObjectTo2D()`
Converts the selected motion object to a 2D motion object.

### `frame.convertMotionObjectTo3D()`
Converts the selected motion object to a 3D motion object.

### `frame.convertToFrameByFrameAnimation()`
Converts the current frame to Frame-by-Frame Animation.
- **returns:** Returns boolean. Returns true if the frame contains animation that can be converted to frame by frame animation. For example: return true for Motion Tween fr...

### `frame.duration`
an integer that represents the number of frames in a frame sequence.

### `frame.elements`
an array of Element objects (see Element object). The order of elements is the order in which they are stored in the FLA file. If there are multiple shapes on the Stage, and each is ungrouped, Flash treats them as one element. If each shape is grouped, so there are multiple groups on the Stage, F...

### `Frame.getCustomEase([property])`
returns an array of objects that represent the control points for the cubic Bézier curve that defines the ease curve.
- **params:** property An optional string that specifies the property for which you want to return the custom ease value. Acceptable values are "all", "position", "rotation", "scale", "color", and "filters". The default value is "all".
- **returns:** Returns an array of JavaScript objects, each of which has an x and y property.

### `Frame.getMotionObjectXML()`
Returns a string of the motion XML from the selected motion object.

### `frame.getSoundEnvelope()`
Gets the sound envelope data of any frame.
- **params:** None
- **returns:** Returns a Sound object.

### `frame.getSoundEnvelopeLmits()`
Gets the limits (start, end) for a custom Sound envelope that is applied to the frame sound.
- **params:** None
- **returns:** Returns a structure that contain start and end fields.

### `frame.hasCustomEase`
a Boolean value. If true, the frame gets its ease information from the custom ease curve. If false, the frame gets its ease information from the ease value.

### `Frame.hasMotionPath()`
a Boolean value. Lets you know whether the current selection includes a motion path.

### `Frame.is3DMotionObject()`
a Boolean value. Lets you know whether the current selection is a 3D motion object.

### `frame.isEmpty()`
a Boolean value. Lets you know whether the frame contains any elements.

### `Frame.isMotionObject()`
a Boolean value. Lets you know whether the current selection is a motion object.

### `frame.labelType`
a string that specifies the type of Frame name. Acceptable values are "none", "name", "comment", and "anchor". Setting a label to "none" clears the frame.name property.

### `frame.motionTweenOrientToPath`
a Boolean value that specifies whether the tweened element rotates the element as it moves along a path to maintain its angle with respect to each point on the path ( true) or whether it does not rotate (false). If you want to specify a value for this property, you should set frame.motionTweenRot...

### `frame.motionTweenRotate`
a string that specifies how the tweened element rotates. Acceptable values are "none", "auto", "clockwise", and "counter-clockwise". A value of "auto" means the object will rotate in the direction requiring the least motion to match the rotation of the object in the following keyframe. If you wan...

### `frame.motionTweenRotateTimes`
an integer that specifies the number of times the tweened element rotates between the starting keyframe and the next keyframe.

### `frame.motionTweenScale`
a Boolean value that specifies whether the tweened element scales to the size of the object in the following keyframe, increasing its size with each frame in the tween (true), or doesn’t scale (false).

### `frame.motionTweenSnap`
a Boolean value that specifies whether the tweened element automatically snaps to the nearest point on the motion guide layer associated with this frame’s layer ( true) or not (false).

### `frame.motionTweenSync`
a Boolean value that if set to true, synchronizes the animation of the tweened object with the main timeline.

### `frame.name`
a string that specifies the name of the frame.

### `Frame.selectMotionPath()`
a Boolean value. Selects (true) or deselects (false) the motion path of the current motion object.

### `frame.setCustomEase(property, easeCurve)`
specifies an array of control point and tangent endpoint coordinates that describe a cubic Bézier curve to be used as a custom ease curve. This array is constructed by the horizontal (ordinal: left to right) position of the control points and tangent endpoints.
- **params:** property A string that specifies the property the ease curve should be used for. Acceptable values are "all", "position", "rotation", "scale", "color", and "filters". easeCurve An array of objects that defines the ease curve. Each array element must be a JavaScript object with x and y properties.

### `Frame.setMotionObjectDuration( duration [, stretchExistingKeyframes] )`
sets the duration (the tween span length) of the currently selected motion object.
- **params:** duration Specifies the number of frames for the tween span of the selected motion object. stretchExistingKeyframes A boolean value that determines whether the tween span is stretched, or if frames are added, to the end of the last frame.

### `frame.setMotionObjectXML( xmlstr [, endAtCurrentLocation] )`
applies the specified motion XML to the selected motion object.
- **params:** xmlstr A string value that specifies the XML string. endAtCurrentLocation A boolean value that determines whether the tween starts or ends at the current position.

### `frame.setSoundEnvelope(soundEnv)`
Sets the sound envelope of any frame with sound file. The soundEnv object is an array and every element of array contains the following properties:  mark  leftChannel  rightChannel
- **params:** soundEnv A sound envelope.

### `frame.setSoundEnvelopeLimits(limits)`
Sets the sound envelope limits of any frame with a sound file.
- **params:** limits A structure that contains start and end fields that signify the limits for a custom sound envelope.

### `frame.shapeTweenBlend`
a string that specifies how a shape tween is blended between the shape in the keyframe at the start of the tween and the shape in the following keyframe. Acceptable values are "distributive" and "angular".

### `frame.soundEffect`
a string that specifies effects for a sound that is attached directly to a frame (frame.soundLibraryItem). Acceptable values are "none", "left channel", "right channel", "fade left to right", "fade right to left", "fade in", "fade out", and "custom".

### `frame.soundLibraryItem`
a library item (see SoundItem object) used to create a sound. The sound is attached directly to the frame.

### `frame.soundLoop`
an integer value that specifies the number of times a sound that is attached directly to a frame (frame.soundLibraryItem) plays. If you want to specify a value for this property, set frame.soundLoopMode to "repeat".

### `frame.soundLoopMode`
a string that specifies whether a sound that is attached directly to a frame (frame.soundLibraryItem) should play a specific number of times or loop indefinitely. Acceptable values are "repeat" and "loop". To specify the number of times the sound should play, set a value for frame.soundLoop.

### `frame.soundName`
a string that specifies the name of a sound that is attached directly to a frame (frame.soundLibraryItem), as stored in the library.

### `frame.soundSync`
a string that specifies the sync behavior of a sound that is attached directly to a frame (frame.soundLibraryItem). Acceptable values are "event", "stop", "start", and "stream".

### `frame.startFrame`
the index of the first frame in a sequence.

### `frame.tweenEasing`
an integer that specifies the amount of easing that should be applied to the tweened object. Acceptable values are -100 to 100. To begin the motion tween slowly and accelerate the tween toward the end of the animation, use a value between -1 and -100. To begin the motion tween rapidly and deceler...

### `Frame.tweenInstanceName()`
a string that assigns an instance name to the selected motion object.

### `frame.tweenType`
a string that specifies the type of tween; acceptable values are "motion", "shape", or "none". The value "none" removes the motion tween. Use the timeline.createMotionTween() method to create a motion tween. If you specify "motion", the object in the frame must be a symbol, text field, or grouped...

### `frame.useSingleEaseCurve`
a Boolean value. If true, a single custom ease curve is used for easing information for all properties. If false, each property has its own ease curve. This property is ignored if the frame doesn’t have custom easing applied.

