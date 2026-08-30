
## library  (20)

### `library.addItemToDocument(position [, namePath])`
adds the current or specified item to the Stage at the specified position.
- **params:** position A point that specifies the x,y position of the center of the item on the Stage. namePath A string that specifies the name of the item. If the item is in a folder, you can specify its name and path using slash notation. If namePath is not specified, the current library selection is used. This parameter is optional.
- **returns:** A Boolean value: true if the item is successfully added to the document; false otherwise.

### `library.addNewItem(type [, namePath]) Property Description library.items An array of Item objects in the library library.unusedItems An array of library Items that are not used in the document.`
creates a new item of the specified type in the Library panel and sets the new item to the currently selected item. For more information on importing items into the library, including items such as sounds, see document.importFile().
- **params:** type A string that specifies the type of item to create. The only acceptable values for type are "video", "movie clip", "button", "graphic", "bitmap", "screen", and "folder" (so, for example, you cannot add a sound to the library with this method). Specifying a folder path is the same as using library.newFolder() before calling this method. namePath A string that specifies the name of the item to be added. If the item is in a folder, specify i...
- **returns:** A Boolean value: true if the item is successfully created; false otherwise.

### `library.deleteItem([namePath])`
deletes the current items or a specified item from the Library panel. This method can affect multiple items if several are selected.
- **params:** namePath A string that specifies the name of the item to be deleted. If the item is in a folder, you can specify its name and path using slash notation. If you pass a folder name, the folder and all its items are deleted. If no name is specified, Flash deletes the currently selected item or items. To delete all the items in the Library panel, select all items before using this method. This parameter is optional.
- **returns:** A Boolean value: true if the items are successfully deleted; false otherwise.

### `library.duplicateItem( [ namePath ] )`
makes a copy of the currently selected or specified item. The new item has a default name (such as item copy) and is set as the currently selected item. If more than one item is selected, the command fails.
- **params:** namePath A string that specifies the name of the item to duplicate. If the item is in a folder, you can specify its name and path using slash notation. This parameter is optional.
- **returns:** A Boolean value: true if the item is duplicated successfully; false otherwise. If more than one item is selected, Flash returns false.

### `library.editItem([namePath])`
opens the currently selected or specified item in Edit mode.
- **params:** namePath A string that specifies the name of the item. If the item is in a folder, you can specify its name and path using slash notation. If namePath is not specified, the single selected library item opens in Edit mode. If none or more than one item in the library is currently selected, the first scene in the main timeline appears for editing. This parameter is optional.
- **returns:** A Boolean value: true if the specified item exists and can be edited; false otherwise.

### `library.findItemIndex(namePath)`
returns the library item’s index value (zero-based). The library index is flat, so folders are considered part of the main index. Folder paths can be used to specify a nested item.
- **params:** namePath A string that specifies the name of the item. If the item is in a folder, you can specify its name and path using slash notation.
- **returns:** An integer value representing the item’s zero-based index value.

### `library.getItemProperty(property)`
gets the property for the selected item.
- **params:** property A string. For a list of values that you can use as a property parameter, see the Property summary table for the Item object, along with property summaries for its subclasses.
- **returns:** A string value for the property.

### `library.getItemType([namePath])`
gets the type of object currently selected or specified by a library path.
- **params:** namePath A string that specifies the name of the item. If the item is in a folder, specify its name and path using slash notation. If namePath is not specified, Flash provides the type of the current selection. If more than one item is currently selected and no namePath is provided, Flash ignores the command. This parameter is optional.
- **returns:** A string value specifying the type of object. For possible return values, see item.itemType.

### `library.getSelectedItems()`
gets the array of all currently selected items in the library.
- **params:** None.
- **returns:** An array of values for all currently selected items in the library.

### `library.itemExists(namePath)`
checks to see if a specified item exists in the library.
- **params:** namePath A string that specifies the name of the item. If the item is in a folder, specify its name and path using slash notation.
- **returns:** A Boolean value: true if the specified item exists in the library; false otherwise.

### `library.items`
an array of item objects in the library.

### `library.moveToFolder(folderPath [, itemToMove [, bReplace]])`
moves the currently selected or specified library item to a specified folder. If the folderPath parameter is empty, the items move to the top level.
- **params:** folderPath A string that specifies the path to the folder in the form "FolderName" or "FolderName/FolderName". To move an item to the top level, specify an empty string ("") for folderPath. itemToMove A string that specifies the name of the item to move. If itemToMove is not specified, the currently selected items move. This parameter is optional. bReplace A Boolean value. If an item with the same name already exists, specifying true for the b...
- **returns:** A Boolean value: true if the item moves successfully; false otherwise.

### `library.newFolder([folderPath])`
creates a new folder with the specified name, or a default name ("untitled folder #") if no folderName parameter is provided, in the currently selected folder.
- **params:** folderPath A string that specifies the name of the folder to be created. If it is specified as a path, and the path doesn’t exist, the path is created. This parameter is optional.
- **returns:** A Boolean value: true if folder is created successfully; false otherwise.

### `library.renameItem(name)`
renames the currently selected library item in the Library panel.
- **params:** name A string that specifies a new name for the library item.
- **returns:** A Boolean value of true if the name of the item changes successfully, false otherwise. If multiple items are selected, no names are changed, and the return v...

### `library.selectAll([bSelectAll])`
selects or deselects all items in the library.
- **params:** bSelectAll A Boolean value that specifies whether to select or deselect all items in the library. Omit this parameter or use the default value of true to select all the items in the library; false deselects all library items. This parameter is optional.

### `library.selectItem(namePath [, bReplaceCurrentSelection [, bSelect]])`
selects a specified library item.
- **params:** namePath A string that specifies the name of the item. If the item is in a folder, you can specify its name and path using slash notation. bReplaceCurrentSelection A Boolean value that specifies whether to replace the current selection or add the item to the current selection. The default value is true (replace current selection). This parameter is optional. bSelect A Boolean value that specifies whether to select or deselect an item. The defa...
- **returns:** A Boolean value: true if the specified item exists; false otherwise.

### `library.selectNone()`
deselects all the library items.
- **params:** None.

### `library.setItemProperty(property, value)`
sets the property for all selected library items (ignoring folders).
- **params:** property A string that is the name of the property to set. For a list of properties, see the Property summary table for the Item object and property summaries for its subclasses. To see which objects are subclasses of the Item object, see “Summary of the DOM structure” on page 14. value The value to assign to the specified property.

### `library.unusedItems`
an array of Library Items that are not used in the document. This is the equivalent of the “Select Unused Items” menu item in the Library panel.

### `library.updateItem([namePath])`
updates the specified item.
- **params:** namePath A string that specifies the name of the item. If the item is in a folder, specify its name and path using slash notation. This is the same as right-clicking on an item and selecting Update from the menu in the user interface. If no name is provided, the current selection is updated. This parameter is optional.
- **returns:** A Boolean value: true if Flash updated the item successfully; false otherwise.

