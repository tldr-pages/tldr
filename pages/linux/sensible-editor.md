# sensible-editor

> Open the default editor.

- Open a file in the default editor:

`sensible-editor {{file}}`

- Open a file in the default editor, with the cursor at the end of the file:

`sensible-editor + {{file}}`

- Open a file in the default editor, with the cursor at the beginning of line 10:

`sensible-editor +10 {{file}}`

- Open 3 files in vertically split editor windows at the same time:

`sensible-editor -O3 {{file_1}} {{file_2}} {{file_3}}`
