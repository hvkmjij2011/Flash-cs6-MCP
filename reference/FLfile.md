
## FLfile  (16)

### `FLfile.copy(fileURI, copyURI)`
copies a file from one location to another. This method returns false if copyURI already exists.
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the file you want to copy. copyURI A string, expressed as a file:/// URI, that specifies the location and name of the copied file.
- **returns:** A Boolean value of true if successful; false otherwise.

### `FLfile.createFolder(folderURI)`
creates one or more folders at the specified location. You can create multiple folders at one time. For example, the following command creates both the MyData and the TempData folders if they don’t already exist: FLfile.createFolder("file:///c|/MyData/TempData")
- **params:** folderURI A folder URI that specifies the folder structure you want to create.
- **returns:** A Boolean value of true if successful; false if folderURI already exists.

### `FLfile.exists(fileURI)`
determines whether a specified file exists. If you specify a folder and a filename, the folder must already exist. To create folders, see FLfile.createFolder(). Examples The following example checks for a file called mydata.txt in the temp folder and displays an alert box indicating whether the f...
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the file you want to verify.
- **returns:** A Boolean value of true if successful; false otherwise.

### `FLfile.getAttributes(fileOrFolderURI)`
returns a string representing the attributes of the specified file or folder, or an empty string if the file has no specific attributes (that it, it is not read-only, not hidden, and so on). You should always use FLfile.exists() to test for the existence of a file or folder before using this meth...
- **params:** fileOrFolderURI A string, expressed as a file:/// URI, specifying the file or folder whose attributes you want to retrieve.
- **returns:** A string that represents the attributes of the specified file or folder. Results are unpredictable if the file or folder doesn’t exist. You should use FLfile...

### `FLfile.getCreationDate(fileOrFolderURI)`
specifies how many seconds have passed between January 1, 1970 and the time the file or folder was created. This method is used primarily to compare the creation or modification dates of files or folders.
- **params:** fileOrFolderURI A string, expressed as a file:/// URI, specifying the file or folder whose creation date and time you want to retrieve as a hexadecimal string.
- **returns:** A string containing a hexadecimal number that represents the number of seconds that have elapsed between January 1, 1970 and the time the file or folder was ...

### `FLfile.getCreationDateObj(fileOrFolderURI)`
returns a JavaScript Date object that represents the date and time when the specified file or folder was created.
- **params:** fileOrFolderURI A string, expressed as a file:/// URI, specifying the file or folder whose creation date and time you want to retrieve as a JavaScript Date object.
- **returns:** A JavaScript Date object that represents the date and time when the specified file or folder was created. If the file doesn’t exist, the object contains info...

### `FLfile.getModificationDate(fileOrFolderURI)`
specifies how many seconds have passed between January 1, 1970 and the time the file or folder was last modified. This method is used primarily to compare the creation or modification dates of files or folders.
- **params:** fileOrFolderURI A string, expressed as a file:/// URI, specifying the file whose modification date and time you want to retrieve as a hexadecimal string.
- **returns:** A string containing a hexadecimal number that represents the number of seconds that have elapsed between January 1, 1970 and the time the file or folder was ...

### `FLfile.getModificationDateObj(fileOrFolderURI)`
returns a JavaScript Date object that represents the date and time when the specified file or folder was last modified.
- **params:** fileOrFolderURI A string, expressed as a file:/// URI, specifying the file or folder whose modification date and time you want to retrieve as a JavaScript Date object.
- **returns:** A JavaScript Date object that represents the date and time when the specified file or folder was last modified. If the file or folder doesn’t exist, the obje...

### `FLfile.getSize(fileURI)`
returns an integer that represents the size of the specified file, in bytes, or 0 if the file doesn’t exist. If the return value is 0, you can use FLfile.exists() to determine whether the file is a zero-byte file or the file doesn’t exist. This method returns correct file size values only for fil...
- **params:** fileURI A string, expressed as a file:/// URI, specifying the file whose size you want to retrieve.
- **returns:** An integer that represents the size of the specified file, in bytes, or 0 if the file doesn’t exist.

### `FLfile.listFolder(folderURI [, filesOrDirectories])`
returns an array of strings representing the contents of the folder. Examples The following example returns three arrays. The first represents all the files in the C:\temp folder, the second represents all the folders in the C:\temp folder, and the third represents the files and folders in the C:...
- **params:** folderURI A string, expressed as a file:/// URI, specifying the folder whose contents you want to retrieve. You can include a wildcard mask as part of folderURI. Valid wildcards are * (matches one or more characters) and ? (matches a single character). filesOrDirectories An optional string that specifies whether to return only filenames or only folder (directory) names. If omitted, both filenames and folder names are returned. Acceptable value...
- **returns:** An array of strings representing the contents of the folder. If the folder doesn’t exist or if no files or folders match the specified criteria, returns an e...

### `FLfile.platformPathToURI(fileName)`
converts a filename in a platform-specific format to a file:/// URI.
- **params:** fileName A string, expressed in a platform-specific format, specifying the filename you want to convert.
- **returns:** A string expressed as a file:/// URI.

### `FLfile.read(fileURI)`
returns the contents of the specified file as a string, or null if the read fails. Examples The following example reads the file mydata.txt and, if successful, displays an alert box with the contents of the file. var fileURI = "file:///c|/temp/mydata.txt"; var str = FLfile.read( fileURI); if (str...
- **params:** fileURI A string, expressed as a file:/// URI, specifying the text-based file (such as .js, .txt, or .jsfl) that you want to read.
- **returns:** The contents of the specified file as a string, or null if the read fails.

### `FLfile.remove(fileOrFolderURI)`
deletes the specified file or folder. If the folder contains files, those files will be deleted as well. Files with the R (read-only) attribute cannot be removed. Examples The following example warns a user if a file exists and then deletes it if the user chooses to do so: var fileURI = prompt ("...
- **params:** fileOrFolderURI A string, expressed as a file:/// URI, specifying the file or folder you want to remove (delete).
- **returns:** A Boolean value of true if successful; false otherwise.

### `FLfile.setAttributes(fileURI, strAttrs)`
specifies system-level attributes for the specified file. The following values are valid for strAttrs:  N — No specific attributes (not read-only, not hidden, and so on)  A — Ready for archiving (Windows only)  R — Read-only (on the Macintosh, read-only means “locked”)  W — Writable (override...
- **params:** fileURI A string, expressed as a file:/// URI, specifying the file whose attributes you want to set. strAttrs A string specifying values for the attribute(s) you want to set. For acceptable values for strAttrs, see the “Description” section below.
- **returns:** A Boolean value of true if successful. Note: Results are unpredictable if the file or folder doesn’t exist. You should use FLfile.exists() before using this ...

### `FLfile.uriToPlatformPath(fileURI)`
converts a filename expressed as a file:/// URI to a platform-specific format.
- **params:** fileURI A string, expressed as a file:/// URI, specifying the filename you want to convert.
- **returns:** A string representing a platform-specific path.

### `FLfile.write(fileURI, textToWrite, [ , strAppendMode])`
writes the specified string to the specified file (as UTF-8). If the specified file does not exist, it is created. However, the folder in which you are placing the file must exist before you use this method. To create folders, use FLfile.createFolder().
- **params:** fileURI A string, expressed as a file:/// URI, specifying the file to which you want to write. textToWrite A string representing the text you want to place in the file. strAppendMode An optional string with the value "append", which specifies that you want to append textToWrite to the existing file. If omitted, fileURI is overwritten with textToWrite.
- **returns:** A Boolean value of true if successful; false otherwise.

