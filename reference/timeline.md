
## timeline  (51)

### `timeline.addMotionGuide()`
adds a motion guide layer above the current layer and attaches the current layer to the newly added guide layer, converting the current layer to a layer of type "Guided". This method functions only on a layer of type "Normal". It has no effect on a layer whose type is "Folder", "Mask", "Masked", ...
- **params:** None.
- **returns:** An integer that represents the zero-based index of the newly added guide layer. If the current layer type is not of type "Normal", Flash returns -1.

### `timeline.addNewLayer([name] [, layerType [, bAddAbove]])`
adds a new layer to the document and makes it the current layer.
- **params:** name A string that specifies the name for the new layer. If you omit this parameter, a new default layer name is assigned to the new layer (“Layer n,” where n is the total number of layers created and deleted for that particular instance of the file). This parameter is optional. layerType A string that specifies the type of layer to add. If you omit this parameter, a “Normal” type layer is created. This parameter is optional. Acceptable values...
- **returns:** An integer value of the zero-based index of the newly added layer.

### `timeline.clearFrames([startFrameIndex [, endFrameIndex]])`
deletes all the contents from a frame or range of frames on the current layer.
- **params:** startFrameIndex A zero-based index that defines the beginning of the range of frames to clear. If you omit startFrameIndex, the method uses the current selection. This parameter is optional. endFrameIndex A zero-based index that defines the end of the range of frames to clear. The range goes up to, but does not include, endFrameIndex. If you specify only startFrameIndex, endFrameIndex defaults to the value of startFrameIndex. This parameter is...

### `timeline.clearKeyframes([startFrameIndex [, endFrameIndex]])`
converts a keyframe to a regular frame and deletes its contents on the current layer.
- **params:** startFrameIndex A zero-based index that defines the beginning of the range of frames to clear. If you omit startFrameIndex, the method uses the current selection. This parameter is optional. endFrameIndex A zero-based index that defines the end of the range of frames to clear. The range goes up to, but does not include, endFrameIndex. If you specify only startFrameIndex, endFrameIndex defaults to the value of startFrameIndex. This parameter is...

### `timeline.convertToBlankKeyframes([startFrameIndex [, endFrameIndex]])`
converts frames to blank keyframes on the current layer.
- **params:** startFrameIndex A zero-based index that specifies the starting frame to convert to keyframes. If you omit startFrameIndex, the method converts the currently selected frames. This parameter is optional. endFrameIndex A zero-based index that specifies the frame at which the conversion to keyframes will stop. The range of frames to convert goes up to, but does not include, endFrameIndex. If you specify only startFrameIndex, endFrameIndex defaults...

### `timeline.convertToKeyframes([startFrameIndex [, endFrameIndex]])`
converts a range of frames to keyframes (or converts the selection if no frames are specified) on the current layer.
- **params:** startFrameIndex A zero-based index that specifies the first frame to convert to keyframes. If you omit startFrameIndex, the method converts the currently selected frames. This parameter is optional. endFrameIndex A zero-based index that specifies the frame at which conversion to keyframes will stop. The range of frames to convert goes up to, but does not include, endFrameIndex. If you specify only startFrameIndex, endFrameIndex defaults to the...

### `timeline.copyFrames([startFrameIndex [, endFrameIndex]])`
copies a range of frames on the current layer to the clipboard.
- **params:** startFrameIndex A zero-based index that specifies the beginning of the range of frames to copy. If you omit startFrameIndex, the method uses the current selection. This parameter is optional. endFrameIndex A zero-based index that specifies the frame at which to stop copying. The range of frames to copy goes up to, but does not include, endFrameIndex. If you specify only startFrameIndex, endFrameIndex defaults to the value of startFrameIndex. T...

### `timeline.copyLayers([startLayerIndex [, endLayerIndex]])`
Copies the layers that are currently selected in the Timeline, or the layers in the specified range. Optional arguments can be provided in order to specify a layer or range of layers to copy.
- **params:** startLayerIndex Optional. A zero-based index that specifies the beginning of the range of layers to copy. If you omit startLayerIndex, the method uses the current selection. endLayerIndex Optional. A zero-based index that specifies the layer at which to stop copying. The range of layers to copy goes up to and including endLayerIndex. If you specify only startLayerIndex, then endLayerIndex defaults to the value of startLayerIndex.

### `timeline.copyMotion()`
copies motion on selected frames, either from a motion tween or from frame-by-frame animation. You can then use timeline.pasteMotion() to apply the motion to other frames. To copy motion as text (code) that you can paste into a script, see timeline.copyMotionAsAS3().
- **params:** None.

### `timeline.copyMotionAsAS3()`
copies motion on selected frames, either from a motion tween or from frame-by-frame animation, to the clipboard as ActionScript 3.0 code. You can then paste this code into a script. To copy motion in a format that you can apply to other frames, see timeline.copyMotion().
- **params:** None.

### `timeline.createMotionObject([startFrame [,endFrame])`
creates a new motion object. The parameters are optional, and if specified set the timeline selection to the indicated frames prior to creating the motion object.
- **params:** startFrame Specifies the first frame at which to create motion objects. If you omit startFrame, the method uses the current selection; if there is no selection, all frames at the current playhead on all layers are removed. This parameter is optional. endFrame Specifies the frame at which to stop creating motion objects; the range of frames goes up to, but does not include, endFrame. If you specify only startFrame, endFrame defaults to the star...

### `timeline.createMotionTween([startFrameIndex [, endFrameIndex]])`
sets the frame.tweenType property to motion for each selected keyframe on the current layer, and converts each frame’s contents to a single symbol instance if necessary. This property is the equivalent to the Create Motion Tween menu item in the Flash authoring tool.
- **params:** startFrameIndex A zero-based index that specifies the beginning frame at which to create a motion tween. If you omit startFrameIndex, the method uses the current selection. This parameter is optional. endFrameIndex A zero-based index that specifies the frame at which to stop the motion tween. The range of frames goes up to, but does not include, endFrameIndex. If you specify only startFrameIndex, endFrameIndex defaults to the startFrameIndex v...

### `timeline.currentFrame`
the zero-based index for the frame at the current playhead location.

### `timeline.currentLayer`
the zero-based index for the currently active layer. A value of 0 specifies the top layer, a value of 1 specifies the layer below it, and so on.

### `timeline.cutFrames([startFrameIndex [, endFrameIndex]])`
cuts a range of frames on the current layer from the timeline and saves them to the clipboard.
- **params:** startFrameIndex A zero-based index that specifies the beginning of a range of frames to cut. If you omit startFrameIndex, the method uses the current selection. This parameter is optional. endFrameIndex A zero-based index that specifies the frame at which to stop cutting. The range of frames goes up to, but does not include, endFrameIndex. If you specify only startFrameIndex, endFrameIndex defaults to the startFrameIndex value. This parameter ...

### `timeline.cutLayers([startLayerIndex [, endLayerIndex]])`
Cuts the layers that are currently selected in the Timeline, or the layers in the specified range. Optional arguments can be provided in order to specify a layer or range of layers to cut.
- **params:** startLayerIndex Optional. A zero-based index that specifies the beginning of the range of layers to cut. If you omit startLayerIndex, the method uses the current selection. endLayerIndex Optional. A zero-based index that specifies the layer at which to stop cutting. The range of layers to cut goes up to and including endLayerIndex. If you specify only startLayerIndex, then endLayerIndex defaults to the value of startLayerIndex.

### `timeline.deleteLayer([index])`
deletes a layer. If the layer is a folder, all layers within the folder are deleted. If you do not specify the layer index, Flash deletes the currently selected layers.
- **params:** index A zero-based index that specifies the layer to be deleted. If there is only one layer in the timeline, this method has no effect. This parameter is optional.

### `timeline.duplicateLayers([startLayerIndex [, endLayerIndex]])`
Duplicates the layers that are currently selected in the Timeline, or the layers in the specified range. Optional arguments can be provided in order to specify a layer or range of layers to duplicate.
- **params:** startLayerIndex Optional. A zero-based index that specifies the beginning of the range of layers to copy. It also specifies the layer above which the layers on the clipboard are pasted. If you omit startLayerIndex, the method uses the current layer selection. endLayerIndex Optional. A zero-based index that specifies the layer at which to stop copying. The range of layers to copy goes up to and including endLayerIndex. If you specify only start...

### `timeline.expandFolder(bExpand [, bRecurseNestedParents [, index]])`
expands or collapses the specified folder or folders. If you do not specify a layer, this method operates on the current layer.
- **params:** bExpand A Boolean value that, if set to true, causes the method to expand the folder; false causes the method to collapse the folder. bRecurseNestedParents A Boolean value that, if set to true, causes all the layers within the specified folder to be opened or closed, based on the bExpand parameter. This parameter is optional. index A zero-based index of the folder to expand or collapse. Use -1 to apply to all layers (you also must set bRecurse...

### `timeline.findLayerIndex(name)`
finds an array of indexes for the layers with the given name. The layer index is flat, so folders are considered part of the main index.
- **params:** name A string that specifies the name of the layer to find.
- **returns:** An array of index values for the specified layer. If the specified layer is not found, Flash returns undefined.

### `timeline.frameCount`
an integer that represents the number of frames in this timeline’s longest layer.

### `timeline.getBounds([frame [, includeHiddenLayers]])`
returns the bounding rectangle for all elements on all layers on the Timeline, for a given frame.
- **params:** frame The number of the frame for which you want the bounds. Defaults to 1, which is the first frame. This parameter is optional. includeHiddenLayers Indicates whether to include element bounds from hidden layers. Defaults to the SWF publish setting value for "include hidden layers". This parameter is optional.
- **returns:** The bounding rectangle for all elements on all layers on the Timeline, for the specified frame.

### `timeline.getFrameProperty(property [, startframeIndex [, endFrameIndex]])`
retrieves the specified property’s value for the selected frames.
- **params:** property A string that specifies the name of the property for which to get the value. See the Property summary for the Frame object for a complete list of properties. startFrameIndex A zero-based index that specifies the starting frame number for which to get the value. If you omit startFrameIndex, the method uses the current selection. This parameter is optional. endFrameIndex A zero-based index that specifies the end of the range of frames t...
- **returns:** A value for the specified property, or undefined if all the selected frames do not have the same property value.

### `timeline.getGuidelines()`
Method: returns an XML string that represents the current positions of the horizontal and vertical guide lines for a timeline (View > Guides >Show Guides). To apply these guide lines to a timeline, use timeline.setGuidelines().
- **params:** None.
- **returns:** An XML string.

### `timeline.getLayerProperty(property)`
retrieves the specified property’s value for the selected layers.
- **params:** property A string that specifies the name of the property whose value you want to retrieve. For a list of properties, see the Property summary for the Frame object.
- **returns:** The value of the specified property. Flash looks at the layer’s properties to determine the type. If all the specified layers don’t have the same property va...

### `timeline.getSelectedFrames()`
retrieves the currently selected frames in an array.
- **params:** None.
- **returns:** An array containing 3n integers, where n is the number of selected regions. The first integer in each group is the layer index, the second integer is the sta...

### `timeline.getSelectedLayers()`
gets the zero-based index values of the currently selected layers.
- **params:** None.
- **returns:** An array of the zero-based index values of the selected layers.

### `timeline.insertBlankKeyframe([frameNumIndex])`
inserts a blank keyframe at the specified frame index; if the index is not specified, the method inserts the blank keyframe by using the playhead/selection. See also timeline.insertKeyframe().
- **params:** frameNumIndex A zero-based index that specifies the frame at which to insert the keyframe. If you omit frameNumIndex, the method uses the current playhead frame number. This parameter is optional. If the specified or selected frame is a regular frame, the keyframe is inserted at the frame. For example, if you have a span of 10 frames numbered 1-10 and you select Frame 5, this method makes Frame 5 a blank keyframe, and the length of the frame s...

### `timeline.insertFrames([numFrames [, bAllLayers [, frameNumIndex]]])`
inserts the specified number of frames at the specified index. If no parameters are specified, this method works as follows:  If one or more frames are selected, the method inserts the selected number of frames at the location of the first selected frame in the current layer. That is, if frames ...
- **params:** numFrames An integer that specifies the number of frames to insert. If you omit this parameter, the method inserts frames at the current selection in the current layer. This parameter is optional. bAllLayers A Boolean value that, if set to true, causes the method to insert the specified number of frames in the numFrames parameter into all layers; if set to false (the default), the method inserts frames into the current layer. This parameter is...

### `timeline.insertKeyframe([frameNumIndex])`
inserts a keyframe at the specified frame. If you omit the parameter, the method inserts a keyframe using the playhead or selection location. This method works the same as timeline.insertBlankKeyframe() except that the inserted keyframe contains the contents of the frame it converted (that is, it...
- **params:** frameNumIndex A zero-based index that specifies the frame index at which to insert the keyframe in the current layer. If you omit frameNumIndex, the method uses the frame number of the current playhead or selected frame. This parameter is optional.

### `timeline.layerCount`
an integer that represents the number of layers in the specified timeline.

### `timeline.layers`
an array of layer objects.

### `timeline.libraryItem`
If the timeline's libraryItem property is null, the timeline belongs to a scene. If it's not null, you can treat it like a LibraryItem object.

### `timeline.name`
a string that specifies the name of the current timeline. This name is the name of the current scene, screen (slide or form), or symbol that is being edited.

### `timeline.pasteFrames([startFrameIndex [, endFrameIndex]])`
pastes the range of frames from the clipboard into the specified frames.
- **params:** startFrameIndex A zero-based index that specifies the beginning of a range of frames to paste. If you omit startFrameIndex, the method uses the current selection. This parameter is optional. endFrameIndex A zero-based index that specifies the frame at which to stop pasting frames. The method pastes up to, but not including, endFrameIndex. If you specify only startFrameIndex, endFrameIndex defaults to the startFrameIndex value. This parameter i...

### `timeline.pasteLayers([layerIndex])`
Paste layers that have been previously cut or copied above the currently selected layer, or above the specified layer index. If the specified layer is a folder layer, the layers are pasted into the folder. Returns the lowest layer index of the layers that were pasted. This action does not affect ...
- **params:** layerIndex Optional. A zero-based index that specifies the layer above which the layers on the clipboard are pasted. If you omit layerIndex, the method uses the current selection.
- **returns:** Integer indicating the lowest layer index of the layers that were pasted.

### `timeline.pasteMotion()`
pastes the range of motion frames retrieved by timeline.copyMotion() to the Timeline. If necessary, existing frames are displaced (moved to the right) to make room for the frames being pasted.
- **params:** None.

### `timeline.pasteMotionSpecial()`
Pastes motion on selected frames. Applies only to a copied classic tween, not a motion tween. Displays a dialog box whose options let the user choose which parts of a classic tween to apply when pasting: X position, Y position, Horizontal scale, Vertical scale, Rotation and skew, Color, Filters, ...
- **params:** None.

### `timeline.removeFrames([startFrameIndex [,endFrameIndex]])`
deletes the frame.
- **params:** startFrameIndex A zero-based index that specifies the first frame at which to start removing frames. If you omit startFrameIndex, the method uses the current selection; if there is no selection, all frames at the current playhead on all layers are removed. This parameter is optional. endFrameIndex A zero-based index that specifies the frame at which to stop removing frames; the range of frames goes up to, but does not include, endFrameIndex. I...

### `timeline.removeMotionObject([startFrame [,endFrame])`
removes the motion object and converts the frame(s) back to static frames. The parameters are optional, and if specified set the timeline selection to the indicated frames prior to removing the motion object.
- **params:** startFrame Specifies the first frame at which to start removing motion objects. If you omit startFrame, the method uses the current selection; if there is no selection, all frames at the current playhead on all layers are removed. This parameter is optional. endFrame Specifies the frame at which to stop removing motion objects; the range of frames goes up to, but does not include, endFrame. If you specify only startFrame, endFrame defaults to ...

### `timeline.reorderLayer(layerToMove, layerToPutItBy [, bAddBefore])`
moves the first specified layer before or after the second specified layer.
- **params:** layerToMove A zero-based index that specifies which layer to move. layerToPutItBy A zero-based index that specifies which layer you want to move the layer next to. For example, if you specify 1 for layerToMove and 0 for layerToPutItBy, the second layer is placed next to the first layer. bAddBefore Specifies whether to move the layer before or after layerToPutItBy. If you specify false, the layer is moved after layerToPutItBy. The default value...

### `timeline.reverseFrames([startFrameIndex [, endFrameIndex]])`
reverses a range of frames.
- **params:** startFrameIndex A zero-based index that specifies the first frame at which to start reversing frames. If you omit startFrameIndex, the method uses the current selection. This parameter is optional. endFrameIndex A zero-based index that specifies the first frame at which to stop reversing frames; the range of frames goes up to, but does not include, endFrameIndex. If you specify only startFrameIndex, endFrameIndex defaults to the value of start...

### `timeline.selectAllFrames()`
selects all the frames in the current timeline.
- **params:** None.

### `timeline.setFrameProperty(property, value [, startFrameIndex [, endFrameIndex]])`
sets the property of the Frame object for the selected frames.
- **params:** property A string that specifies the name of the property to be modified. For a complete list of properties and values, see the Property summary for the Frame object. You can’t use this method to set values for read-only properties such as frame.duration and frame.elements. value Specifies the value to which you want to set the property. To determine the appropriate values and type, see the Property summary for the Frame object. startFrameInde...

### `timeline.setGuidelines(xmlString)`
Method: replaces the guide lines for the timeline (View > Guides > Show Guides) with the information specified in xmlString. To retrieve an XML string that can be passed to this method, use timeline.getGuidelines(). To view the newly set guide lines, you may have to hide them and then view them.
- **params:** xmlString An XML string that contains information on the guidelines to apply.
- **returns:** A Boolean value of true if the guidelines are successfully applied; false otherwise.

### `timeline.setLayerProperty(property, value [, layersToChange])`
sets the specified property on all the selected layers to a specified value.
- **params:** property A string that specifies the property to set. For a list of properties, see “Layer object” on page 355. value The value to which you want to set the property. Use the same type of value you would use when setting the property in the layer object. layersToChange A string that identifies which layers should be modified. Acceptable values are "selected", "all", and "others". The default value is "selected" if you omit this parameter. This...

### `timeline.setSelectedFrames(startFrameIndex, endFrameIndex [, bReplaceCurrentSelection]) timeline.setSelectedFrames(selectionList [, bReplaceCurrentSelection])`
selects a range of frames in the current layer or sets the selected frames to the selection array passed into this method.
- **params:** startFrameIndex A zero-based index that specifies the beginning frame to set. endFrameIndex A zero-based index that specifies the end of the selection; endFrameIndex is the frame after the last frame in the range to select. bReplaceCurrentSelection A Boolean value that, if it is set to true, causes the currently selected frames to be deselected before the specified frames are selected. The default value is true. selectionList An array of three...

### `timeline.setSelectedLayers(index [, bReplaceCurrentSelection])`
sets the layer to be selected, and also makes the specified layer the current layer. Selecting a layer also means that all the frames in the layer are selected.
- **params:** index A zero-based index for the layer to select. bReplaceCurrentSelection A Boolean value that, if it is set to true, causes the method to replace the current selection; false causes the method to extend the current selection. The default value is true. This parameter is optional.

### `timeline.showLayerMasking([layer])`
shows the layer masking during authoring by locking the mask and masked layers. This method uses the current layer if no layer is specified. If you use this method on a layer that is not of type Mask or Masked, Flash displays an error in the Output panel.
- **params:** layer A zero-based index of a mask or masked layer to show masking during authoring. This parameter is optional.

### `timeline.startPlayback()`
starts automatic playback of the timeline if it is currently playing. This method can be used with SWF panels to control timeline playback in the authoring environment.

### `timeline.stopPlayback()`
stops automatic playback of the timeline if it is currently playing. This method can be used with SWF panels to control timeline playback in the authoring environment.

