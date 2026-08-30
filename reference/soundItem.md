
## soundItem  (14)

### `soundItem.bitRate`
a string that specifies the bit rate of a sound in the library. This property is available only for the MP3 compression type. Acceptable values are "8 kbps", "16 kbps", "20 kbps", "24 kbps", "32 kbps", "48 kbps", "56 kbps", "64 kbps", "80 kbps", "112 kbps", "128 kbps", and "160 kbps". Stereo soun...

### `soundItem.bits`
a string that specifies the bits value for a sound in the library that has ADPCM compression. Acceptable values are "2 bit", "3 bit", "4 bit", and "5 bit". soundItem.sourceFileIsCurrent Read-only; a Boolean value that specifies whether the file modification date of the Library item is the same as...

### `soundItem.compressionType`
a string that specifies that compression type for a sound in the library. Acceptable values are "Default", "ADPCM", "MP3", "Raw", and "Speech". If you want to specify a value for this property, set soundItem.useImportedMP3Quality to false.

### `soundItem.convertStereoToMono`
a Boolean value available only for MP3 and Raw compression types. Setting this value to true converts a stereo sound to mono; false leaves it as stereo. For the MP3 compression type, if soundItem.bitRate is less than 20 Kbps, this property is ignored and forced to true (see soundItem.bitRate). If...

### `soundItem.exportToFile(fileURI)`
exports the specified item to a WAV or MP3 file. Export settings are based on the item being exported. When exporting sound items, you should check if the soundItem.originalCompressionType property is equal to"RAW." If this check is false, you can only export the file as MP3. (Optionally, you can...
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the path and name of the exported file.
- **returns:** A Boolean value of true if the file was exported successfully; false otherwise.

### `soundItem.fileLastModifiedDate`
Read-only property: a string containing a hexadecimal number that represents the number of seconds that have elapsed between January 1, 1970, and the modification date of the original file (on disk) at the time the file was imported to the library. If the file no longer exists, this value is "000...

### `soundItem.lastModifiedDate`
a hexadecimal value indicating the modification date and time of the sound item. This value is incremented every time the sound item is imported. For example, selecting the Update button from the Sound Properties dialog will trigger an import.

### `soundItem.originalCompressionType`
Read-only property: a string that specifies whether the specified item was imported as an mp3 file. Possible values for this property are “RAW” and “MP3”.

### `soundItem.quality`
a string that specifies the playback quality of a sound in the library. This property is available only for the MP3 compression type. Acceptable values are "Fast", "Medium", and "Best". If you want to specify a value for this property, set soundItem.useImportedMP3Quality to false.

### `soundItem.sampleRate`
a string that specifies the sample rate for the audio clip. This property is available only for the ADPCM, Raw, and Speech compression types. Acceptable values are "5 kHz", "11 kHz", "22 kHz", and "44 kHz". If you want to specify a value for this property, set soundItem.useImportedMP3Quality to f...

### `soundItem.sourceFileExists`
Read-only property: a Boolean value of true if the file that was imported to the Library still exists in the location from where it was imported; false otherwise.

### `soundItem.sourceFileIsCurrent`
Read-only property: a Boolean value of true if the file modification date of the Library item is the same as the modification date on disk of the file that was imported; false otherwise.

### `soundItem.sourceFilePath`
Read-only property: a string, expressed as a file:/// URI, that represents the path and name of the file that was imported into the Library.

### `soundItem.useImportedMP3Quality`
a Boolean value. If true, all other properties are ignored, and the imported MP3 quality is used.

