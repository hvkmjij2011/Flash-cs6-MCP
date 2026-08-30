
## text  (31)

### `text.accName`
a string that is equivalent to the Name field in the Accessibility panel. Screen readers identify objects by reading the name aloud. This property cannot be used with dynamic text. text.embeddedCharacters A string that specifies characters to embed. This is equivalent to entering text in the Char...

### `text.antiAliasSharpness`
a float value that specifies the anti-aliasing sharpness of the text. This property controls how crisply the text is drawn; higher values specify sharper (or crisper) text. A value of 0 specifies normal sharpness. This property is available only if text.fontRenderingMode is set to customThickness...

### `text.antiAliasThickness`
a float value that specifies the anti-aliasing thickness of the text. This property controls how thickly the text is drawn, with higher values specifying thicker text. A value of 0 specifies normal thickness. This property is available only if text.fontRenderingMode is set to customThicknessSharp...

### `text.autoExpand`
a Boolean value. For static text fields, a value of true causes the bounding width to expand to show all text. For dynamic or input text fields, a value of true causes the bounding width and height to expand to show all text.

### `text.border`
a Boolean value. A value of true causes Flash to show a border around text.

### `text.description`
a string that is equivalent to the Description field in the Accessibility panel. The description is read by the screen reader.

### `text.embedRanges`
a string that consists of delimited integers that correspond to the items that can be selected in the Character Embedding dialog box. This property works only with dynamic or input text; it is ignored if used with static text. This property corresponds to the XML file in the Configuration/Font Em...

### `text.embedVariantGlyphs`
a Boolean value that specifies whether to enable the embedding of variant glyphs (true) or not (false). This property works only with dynamic or input text; it is ignored if used with static text. The default value is false. Note: Beginning in Flash Professional CS5, font embedding is controlled ...

### `text.embeddedCharacters`
a string that specifies characters to embed. This is equivalent to entering text in the Character Embedding dialog box. This property works only with dynamic or input text; it generates a warning if used with other text types. Note: Beginning in Flash Professional CS5, font embedding is controlle...

### `text.filters`
an array of filters applied to the text element. To modify filter properties, you don’t write to this array directly. Instead, retrieve the array, set the individual properties, and then set the array to reflect the new properties.

### `text.fontRenderingMode`
a string that specifies the rendering mode for the text. This property affects how the text is displayed both on the Stage and in Flash Player. Acceptable values are described in the following table: Property value How text is rendered device Renders the text with device fonts. bitmap Renders ali...

### `text.getTextAttr(attrName [, startIndex [, endIndex]])`
retrieves the attribute specified by the attrName parameter for the text identified by the optional startIndex and endIndex parameters. If the attribute is not consistent for the specified range, Flash returns undefined. If you omit the optional parameters startIndex and endIndex, the method uses...
- **params:** attrName A string that specifies the name of the TextAttrs object property to be returned. For a list of possible values for attrName, see the Property summary for the TextAttrs object. startIndex An integer that is the index of first character. This parameter is optional. endIndex An integer that specifies the end of the range of text, which starts with startIndex and goes up to, but does not include, endIndex. This parameter is optional.
- **returns:** The value of the attribute specified in the attrName parameter.

### `text.getTextString([startIndex [, endIndex]])`
retrieves the specified range of text. If you omit the optional parameters startIndex and endIndex, the whole text string is returned. If you specify only startIndex, the method returns the string starting at the index location and ending at the end of the field. If you specify both startIndex an...
- **params:** startIndex An integer that specifies the index (zero-based) of the first character. This parameter is optional. endIndex An integer that specifies the end of the range of text, which starts from startIndex and goes up to, but does not include, endIndex. This parameter is optional.
- **returns:** A string of the text in the specified range.

### `text.length`
an integer that represents the number of characters in the Text object.

### `text.lineType`
a string that sets the line type. Acceptable values are "single line", "multiline", "multiline no wrap", and "password". This property works only with dynamic or input text and generates a warning if used with static text. The "password" value works only for input text.

### `text.maxCharacters`
an integer that specifies the maximum number of characters the user can enter in this Text object. This property works only with input text; if used with other text types, the property generates a warning.

### `text.orientation`
a string that specifies the orientation of the text field. Acceptable values are "horizontal", "vertical left to right", and "vertical right to left". This property works only with static text; it generates a warning if used with other text types.

### `text.renderAsHTML`
a Boolean value. If the value is true, Flash draws the text as HTML and interprets embedded HTML tags. This property works only with dynamic or input text; it generates a warning if used with other text types.

### `text.scrollable`
a Boolean value. If the value is true, the text can be scrolled. This property works only with dynamic or input text; it generates a warning if used with static text.

### `text.selectable`
a Boolean value. If the value is true, the text can be selected. Input text is always selectable. Flash generates a warning when this property is set to false and used with input text.

### `text.selectionEnd`
a zero-based integer that specifies the end of a text subselection. For more information, see text.selectionStart.

### `text.selectionStart`
a zero-based integer that specifies the beginning of a text subselection. You can use this property with text.selectionEnd to select a range of characters. Characters up to, but not including, text.selectionEnd are selected. See text.selectionEnd.  If there is an insertion point or no selection,...

### `text.setTextAttr(attrName, attrValue [, startIndex [, endIndex]])`
sets the attribute specified by the attrName parameter associated with the text identified by startIndex and endIndex to the value specified by attrValue. This method can be used to change attributes of text that might span TextRun elements (see TextRun object), or that are portions of existing T...
- **params:** attrName A string that specifies the name of the TextAttrs object property to change. attrValue The value for the TextAttrs object property. For a list of possible values for attrName and attrValue, see the Property summary for the TextAttrs object. startIndex An integer that is the index (zero-based) of the first character in the array. This parameter is optional. endIndex An integer that specifies the index of the end point in the selected t...

### `text.setTextString(text [, startIndex [, endIndex]])`
changes the text string within this Text object. If you omit the optional parameters, the whole Text object is replaced. If you specify only startIndex, the specified string is inserted at the startIndex position. If you specify both startIndex and endIndex, the specified string replaces the segm...
- **params:** text A string that consists of the characters to be inserted into this Text object. startIndex An integer that specifies the index (zero-based) of the character in the string where the text will be inserted. This parameter is optional. endIndex An integer that specifies the index of the end point in the selected text string. The new text overwrites the text from startIndex up to, but not including, endIndex. This parameter is optional.

### `text.shortcut`
a string that is equivalent to the Shortcut field in the Accessibility panel. The shortcut is read by the screen reader. This property cannot be used with dynamic text.

### `text.silent`
a Boolean value that specifies whether the object is accessible. This is equivalent to the inverse logic of the Make Object Accessible setting in the Accessibility panel. That is, if silent is true, Make Object Accessible is deselected. If it is false, Make Object Accessible is selected.

### `text.tabIndex`
an integer that is equivalent to the Tab Index field in the Accessibility panel. This value lets you determine the order in which objects are accessed when the user presses the Tab key.

### `text.textRuns`
an array of TextRun objects (see TextRun object).

### `text.textType`
a string that specifies the type of text field. Acceptable values are "static", "dynamic", and "input".

### `text.useDeviceFonts`
a Boolean value. A value of true causes Flash to draw text using device fonts.

### `text.variableName`
a string that contains the name of the variable associated with the Text object. This property works only with dynamic or input text; it generates a warning if used with other text types. This property is supported only in ActionScript 1.0 and ActionScript 2.0.

