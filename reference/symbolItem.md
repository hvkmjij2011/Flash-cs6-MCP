
## symbolItem  (13)

### `symbolItem.convertToCompiledClip()`
converts a symbol item in the library to a compiled movie clip.
- **params:** None.

### `symbolItem.exportSWC(outputURI)`
exports the symbol item to a SWC file.
- **params:** outputURI A string, expressed as a file:/// URI, that specifies the SWC file to which the method will export the symbol. The outputURI must reference a local file. Flash does not create a folder if outputURI does not exist.

### `symbolItem.exportSWF(outputURI)`
exports the symbol item to a SWF file.
- **params:** outputURI A string, expressed as a file:/// URI, that specifies the SWF file to which the method will export the symbol. The outputURI must reference a local file. Flash does not create a folder if outputURI doesn’t exist.

### `symbolItem.exportToLibrary(frameNumber, bitmapName)`
exports a frame from the selected instance of movie clip, graphic, or button symbol on the Stage to a bitmap in Library.
- **params:** frameNumber An integer indicating the frame within the symbol to be exported. bitmapName A string indicating the name of the new bitmap to be added to the Library.

### `symbolItem.exportToPNGSequence(outputURI [, startFrameNum ][, endFrameNum ] [, matrix])`
exports a movie clip, graphic, or button symbol to a sequence of PNG files on disk.
- **params:** outputURI The URI to export the PNG sequence files to. This URI must reference a local file. For example: file:///c|/tests/mytest.png. startFrameNum An integer indicating the first frame within the symbol to be exported. If this parameter is omitted, all frames are exported. endFrameNum An integer indicating the last frame within the symbol to be exported. If this parameter is omitted, all frames are exported. matrix Optional. A matrix to be a...

### `symbolItem.lastModifiedDate`
a string that indicates the modification date of the symbol as a hexadecimal value, representing a date and time. This value is incremented every time a symbol's timeline is edited.

### `symbolItem.scalingGrid`
a Boolean value that specifies whether 9-slice scaling is enabled for the item.

### `symbolItem.scalingGridRect`
a Rectangle object that specifies the locations of the four 9-slice guides. For information on the format of the rectangle, see document.addNewRectangle().

### `symbolItem.sourceAutoUpdate`
a Boolean value that specifies whether the item is updated when the FLA file is published. The default value is false. Used for shared library symbols.

### `symbolItem.sourceFilePath`
a string that specifies the path for the source FLA file as a file:/// URI. The path must be an absolute path, not a relative path. This property is used for shared library symbols.

### `symbolItem.sourceLibraryName`
a string that specifies the name of the item in the source file library. It is used for shared library symbols.

### `symbolItem.symbolType`
a string that specifies the type of symbol. Acceptable values are "movie clip", "button", and "graphic".

### `symbolItem.timeline`
a Timeline object.

