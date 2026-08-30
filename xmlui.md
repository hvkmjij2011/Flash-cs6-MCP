
## xmlui  (11)

### `xmlui.accept()`
closes the current XMLUI dialog box with an accept state, which is equivalent to the user clicking the OK button.
- **params:** None.

### `xmlui.cancel()`
closes the current XMLUI dialog box with a cancel state, which is equivalent to the user clicking the Cancel button.
- **params:** None.

### `xmlui.get(controlPropertyName)`
retrieves the value of the specified property of the current XMLUI dialog box.
- **params:** controlPropertyName A string that specifies the name of the XMLUI property whose value you want to retrieve.
- **returns:** A string that represents the value of the specified property. In cases where you might expect a Boolean value of true or false, it returns the string "true" ...

### `xmlui.getControlItemElement(controlPropertyName)`
returns the label and value of the line selected in a ListBox or ComboBox control for the control specified by controlPropertyName.
- **params:** controlPropertyName A string that specifies the property whose control item element you want to retrieve.
- **returns:** An object that represents the current control item for the control specified by controlPropertyName.

### `xmlui.getEnabled(controlID)`
returns a Boolean value that specifies whether the control is enabled or disabled (dimmed).
- **params:** controlID A string that specifies the ID attribute of the control whose status you want to retrieve.
- **returns:** A Boolean value of true if the control is enabled; false otherwise.

### `xmlui.getVisible(controlID)`
returns a Boolean value that specifies whether the control is visible or hidden.
- **params:** controlID A string that specifies the ID attribute of the control whose visibility status you want to retrieve.
- **returns:** A Boolean value of true if the control is visible, or false if it is invisible (hidden).

### `xmlui.set(controlPropertyName, value)`
modifies the value of the specified property of the current XMLUI dialog box.
- **params:** controlPropertyName A string that specifies the name of XMLUI property to modify. value A string that specifies the value to which you want to set the XMLUI property.

### `xmlui.setControlItemElement(controlPropertyName, elementItem)`
sets the label and value of the currently selected line in the ListBox or ComboBox control specified by controlPropertyName.
- **params:** controlPropertyName A string that specifies the control item element to set. elementItem A JavaScript object with a string property named label and an optional string property named value. If the value property does not exist, then it is created and assigned the same value as label.

### `xmlui.setControlItemElements(controlID, elementItemArray)`
clears the values of the ListBox or ComboBox control specified by controlID and replaces the list or menu items with the label, value pairs specified by elementItemArray.
- **params:** controlID A string that specifies the ID attribute of the control you want to set. elementItemArray An array of JavaScript objects, where each object has a string property named label and an optional string property named value. If the value property does not exist, then it is created and assigned the same value as label.

### `xmlui.setEnabled(controlID, enable)`
enables or disables (dims) a control.
- **params:** controlID A string that specifies the ID attribute of the control you want to enable or disable. enable A Boolean value of true if you want to enable the control, or false if you want to disable (dim) it.

### `xmlui.setVisible(controlID, visible)`
shows or hides a control.
- **params:** controlID A string that specifies the ID attribute of the control you want to show or hide. visible A Boolean value of true if you want to show the control; false if you want to hide it.

