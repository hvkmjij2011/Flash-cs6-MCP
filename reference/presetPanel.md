
## presetPanel  (14)

### `fl. presetPanel.addNewItem( [namePath] );`
if a single motion tween is currently selected on the Stage, adds that motion to the Motion Presets panel in the specified folder with the specified name. The path specified in namePath must exist in the panel. If a preset matching namePath exists, this method has no effect, and returns false. If...
- **params:** namePath A string that specifies the path and name of the item to add to the Motion Presets panel. This parameter is optional.
- **returns:** A Boolean value of true if the item was successfully added; false otherwise.

### `presetPanel.applyPreset( [presetPath] )`
applies the specified or currently selected preset to the currently selected item on the Stage. The item must be a motion tween, a symbol, or an item that can be converted to a symbol. If the item is a motion tween, its current motion is replaced with the selected preset without requesting user c...
- **params:** presetPath A string that specifies the full path and name of the preset to be applied, as it appears in the Motion Presets panel. This parameter is optional; if you don’t pass a value, the currently selected preset is applied.
- **returns:** A Boolean value of true if the preset is successfully applied, false otherwise.

### `presetPanel.deleteFolder( [folderPath])`
deletes the specified folder and any of its subfolders from the folder tree of the Motion Presets panel. Any presets in the folders are also deleted. You can’t delete folders from the Default Presets folder. If you don’t pass a value for folderPath, any folders that are currently selected are del...
- **params:** folderPath A string that specifies the folder to delete from the Motion Presets panel. This parameter is optional.
- **returns:** A Boolean value of true if the folder or folders are successfully deleted; false otherwise.

### `presetPanel.deleteItem( [namePath] )`
deletes the specified preset from the Motion Presets panel. If you don’t pass a value for namePath, any presets that are currently selected are deleted. You can’t delete items from the Default Presets folder. Note: Items are deleted without requesting user confirmation, and there is no way to und...
- **params:** namePath A string that specifies the path and name of the item to delete from the Motion Presets panel. This parameter is optional.
- **returns:** A Boolean value of true if the item or items are successfully deleted; false otherwise.

### `presetPanel.expandFolder( [bExpand [, bRecurse [, folderPath] ] ] )`
expands or collapses the currently selected folder or folders in the Motion Presets panel. To expand or collapse folders other than the folders that are currently selected, pass a value for folderPath.
- **params:** bExpand A Boolean value that specifies whether to expand the folder (true) or collapse it (false). This parameter is optional; the default value is true. bRecurse A Boolean value that specifies whether to expand or collapse the folder’s subfolders (true) or not false). This parameter is optional; the default value is false. folderPath A string that specifies the path to the folder to expand or collapse. This parameter is optional.
- **returns:** A Boolean value of true if the folder or folders are successfully expanded or collapsed; false otherwise.

### `presetPanel.exportItem(fileURI [, namePath] )`
exports the currently selected or the specified preset to an XML file. Only presets can be exported; the method fails if you try to export a folder. This method also fails if you try to overwrite a file on disk. If you don’t specify a filename as part of fileURI (that is, if the last character of...
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the path and optionally a filename for the exported file. See “Description,” below, for more information. namePath A string that specifies the path and name of the item to select from the Motion Presets panel. This parameter is optional.
- **returns:** A Boolean value of true if the preset was exported successfully; false otherwise.

### `presetPanel.findItemIndex([presetName])`
returns an integer that represents the index location of an item in the Motion Presets panel.
- **params:** presetName A string that specifies the name of the preset for which the index value is returned. This parameter is optional.
- **returns:** An integer that represents the index of the specified preset in the presetPanel.items array. If you don’t pass a value for presetName, the index of the curre...

### `presetPanel.getSelectedItems()`
returns an array of presetItem objects corresponding to the currently selected items in the Motion Presets panel (see presetItem object). Each item in the array represents either a folder or a preset.
- **params:** None.
- **returns:** An array of presetItem objects.

### `presetPanel.importItem(fileURI [,namePath ])`
adds a preset to the Motion Presets panel from a specified XML file. The path specified in namePath must exist in the panel. To create XML files that can be imported, use presetPanel.exportItem(). If you don’t pass a value for namePath, the imported preset is placed in the Custom Presets folder a...
- **params:** fileURI A string, expressed as a file:/// URI, that specifies the XML file to be imported as a preset in the Motion Presets panel. namePath A string that specifies in which folder to place the imported file and what to name it. This parameter is optional.
- **returns:** A Boolean value of true if the file is successfully imported; false otherwise.

### `presetPanel.items`
an array of presetItem objects in the Motion Presets panel (see presetItem object). Each item in the array represents either a folder or a preset.

### `presetPanel.moveToFolder(folderPath [, namePath] )`
moves the specified item to the specified folder. If you pass an empty string ("") for folderPath, the items are moved to the Custom Presets folder. If you don’t pass a value for namePath, the currently selected items are moved. You can’t move items to or from the Default Presets folder.
- **params:** folderPath A string that specifies the path to the folder in the Motion Presets panel to which the item or items are moved. namePath A string that specifies the path and name of the item to move. This parameter is optional.
- **returns:** A Boolean value of true if the items are successfully moved; false otherwise.

### `presetPanel.newFolder( [folderPath] )`
creates a folder in the folder tree of the Motion Presets panel. You can create only one new folder level with this method. That is, if you pass “Custom Presets/My First Folder/My Second Folder" for folderPath, “Custom Presets/My First Folder“ must exist in the folder tree. If you don’t pass a va...
- **params:** folderPath A string that specifies where to add a new folder in the Motion Presets panel, and the name of the new folder. This parameter is optional.
- **returns:** A Boolean value of true if the folder is successfully added; false otherwise.

### `presetPanel.renameItem(newName)`
renames the currently selected preset or folder to a specified name. This method succeeds only if a single preset or folder in the Custom Presets folder is selected. This method fails in the following situations:  No item is selected.  Multiple items are selected.  The selected item is in the ...
- **params:** newName A string that specifies the new name for the preset or folder.
- **returns:** A Boolean value of true if the preset or folder is successfully renamed; false otherwise.

### `presetPanel.selectItem(namePath [, bReplaceCurrentSelection [, bSelect] ])`
selects or deselects an item in the Motion Presets panel, optionally replacing any items currently selected.
- **params:** namePath A string that specifies the path and name of the item to select from the Motion Presets panel. bReplaceCurrentSelection A Boolean value that specifies whether the specified item replaces any current selection (true) or is added to the current selection (false). This parameter is optional; the default value is true. bSelect A Boolean value that specifies whether to select the item (true) or deselect the item (false). This parameter is ...
- **returns:** A Boolean value of true if the item was successfully selected or deselected; false otherwise.

