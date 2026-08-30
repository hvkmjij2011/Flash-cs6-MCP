
## item  (16)

### `item.addData(name, type, data)`
adds specified data to a library item.
- **params:** name A string that specifies the name of the data. type A string that specifies the type of data. Valid types are "integer", "integerArray", "double", "doubleArray", "string", and "byteArray". data The data to add to the specified library item. The type of data depends on the value of the type parameter. For example, if type is "integer", the value of data must be an integer, and so on.

### `item.getData(name)`
retrieves the value of the specified data.
- **params:** name A string that specifies the name of the data to retrieve.
- **returns:** The data specified by the name parameter. The type of data returned depends on the type of stored data.

### `library.getPublishData(name, format)`
Indicates whether publishing of the specified persistent data is enabled for the specified format on a specified library item.
- **params:** name A string that contains the name of the persistent data item, as specified in “item.addData()” on page 345. format A string that specifies the publishing format. Note: _EMBED_SWF_ is a special built-in publishing format for persistent data. If set, the persistent data is embedded in the SWF file every time a document is published. The persistent data can then be accessed via ActionScript with the .metaData property. This feature applies to...
- **returns:** A Boolean value that indicates whether publishing of the specified persistent data is enabled for the specified format on this library item.

### `item.hasData(name)`
determines whether the library item has the named data.
- **params:** name A string that specifies the name of the data to check for in the library item.
- **returns:** A Boolean value: true if the specified data exists; false otherwise.

### `item.itemType`
a string that specifies the type of element. The value is one of the following: "undefined", "component", "movie clip", "graphic", "button", "folder", "font", "sound", "bitmap", "compiled clip", "screen", or "video". If this property is "video", you can determine the type of video; see videoItem....

### `item.linkageBaseClass`
a string that specifies the ActionScript 3.0 class that will be associated with the symbol. The value specified here appears in the Linkage dialog box in the authoring environment, and in other dialog boxes that include the Linkage dialog box controls, such as the Symbol Properties dialog box. (T...

### `item.linkageClassName`
a string that specifies the ActionScript 2.0 class that will be associated with the symbol. (To specify this value for an ActionScript 3.0 class, use item.linkageBaseClass.) For this property to be defined, the item.linkageExportForAS and/or item.linkageExportForRS properties must be set to true,...

### `item.linkageExportForAS`
a Boolean value. If this property is true, the item is exported for ActionScript. You can also set the item.linkageExportForRS and item.linkageExportInFirstFrame properties to true. If you set this property to true, the item.linkageImportForRS property must be set to false. Also, you must specify...

### `item.linkageExportForRS`
a Boolean value. If this property is true, the item is exported for run-time sharing. You can also set the item.linkageExportForAS and item.linkageExportInFirstFrame properties to true. If you set this property to true, the item.linkageImportForRS property must be set to false. Also, you must spe...

### `item.linkageExportInFirstFrame`
a Boolean value. If true, the item is exported in the first frame; if false, the item is exported in the frame of the first instance. If the item does not appear on the Stage, it isn’t exported. This property can be set to true only when item.linkageExportForAS and/or item.linkageExportForRS are ...

### `item.linkageIdentifier`
a string that specifies the name Flash will use to identify the asset when linking to the destination SWF file. Flash ignores this property if item.linkageImportForRS, item.linkageExportForAS, and item.linkageExportForRS are set to false. Conversely, this property must be set when any of those pr...

### `item.linkageImportForRS`
a Boolean value: if true, the item is imported for run-time sharing. If this property is set to true, both item.linkageExportForAS and item.linkageExportForRS must be set to false. Also, you must specify an identifier (item.linkageIdentifier) and a URL (item.linkageURL).

### `item.linkageURL`
a string that specifies the URL where the SWF file containing the shared asset is located. Flash ignores this property if item.linkageImportForRS, item.linkageExportForAS, and item.linkageExportForRS are set to false. Conversely, this property must be set when any of those properties are set to t...

### `item.name`
a string that specifies the name of the library item, which includes the folder structure. For example, if Symbol_1 is inside a folder called Folder_1, the name property of Symbol_1 is "Folder_1/Symbol_1".

### `item.removeData(name)`
removes persistent data from the library item.
- **params:** name Specifies the name of the data to remove from the library item.

### `library.setPublishData(name, format, publish)`
Enables publishing of persistent data for a library item.
- **params:** name A string that contains the name of the persistent data item, as specified in “item.addData()” on page 345. format A string that specifies the publishing format. Note: _EMBED_SWF_ is a special built-in publishing format for persistent data. If set, the persistent data is embedded in the SWF file every time a document is published. The persistent data can then be accessed via ActionScript with the .metaData property. This feature applies to...
- **returns:** None.

