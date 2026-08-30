
## bitmapItem  (15)

### `bitmapItem.allowSmoothing`
a Boolean value that specifies whether to allow smoothing of a bitmap (true) or not (false).

### `bitmapItem.compressionType`
a string that determines the type of image compression applied to the bitmap. Acceptable values are "photo" or "lossless". If the value of bitmapItem.useImportedJPEGQuality is false, "photo" corresponds to JPEG with a quality from 0 to 100; if bitmapItem.useImportedJPEGQuality is true, "photo" co...

### `bitmapItem.exportToFile(fileURI, quality)`
exports the specified item to a PNG or JPG file.
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the path and name of the exported file. quality A number, from 1-100, that determines the quality of the exported image file. A higher number indicates higher quality. The default is 80. New in Flash CS6 Professional.
- **returns:** A Boolean value of true if the file was exported successfully; false otherwise.

### `bitmapItem.fileLastModifiedDate`
a string containing a hexadecimal number that represents the number of seconds that have elapsed between January 1, 1970 and the modification date of the original file at the time the file was imported to the library. If the file no longer exists, this value is "00000000".

### `bitmapItem.hPixels`
an int that specifies the width of the bitmap, in pixels.

### `bitmapItem.hasValidAlphaLayer`
a boolean indicating if a bitmap in the library has a valid/useful alpha channel. This flag will help you decide if you should export the bitmap item as a PNG instead of a JPEG using the bitmapItem.exportToFile() function.

### `bitmapItem.lastModifiedDate`
a hexadecimal value indicating the modification date and time of the bitmap item. This value is incremented every time the bitmap item is imported. For example, selecting the Update button from the Bitmap Properties dialog will trigger an import.

### `bitmapItem.originalCompressionType`
a string that specifies whether the specified item was imported as an jpeg file. Possible values for this property are “photo” (for jpeg files) and “lossless” (for uncompressed file types such as GIF and PNG).

### `bitmapItem.quality`
an integer that specifies the quality of the bitmap. To use the default document quality, specify -1; otherwise, specify an integer from 0 to 100. Available only for JPEG compression.

### `bitmapItem.sourceFileExists`
a Boolean value of true if the file that was imported to the Library still exists in the location from where it was imported; false otherwise.

### `bitmapItem.sourceFileIsCurrent`
a Boolean value of true if the file modification date of the Library item is the same as the modification date on disk of the file that was imported ;false otherwise.

### `bitmapItem.sourceFilePath`
a string, expressed as a file:/// URI, that represents the path and name of the file that was imported into the Library.

### `bitmapItem.useDeblocking`
a Boolean value that specifies whether deblocking is enabled (true) or not (false).

### `bitmapItem.useImportedJPEGQuality`
a Boolean value that specifies whether to use the default imported JPEG quality (true) or not (false). Available only for JPEG compression.

### `bitmapItem.vPixels`
an int that specifies the height of the bitmap, in pixels.

