# sensible-editor

> Open the default editor.
> More information: <https://manned.org/sensible-editor>.

- Open a file in the default editor:

`sensible-editor {{path/to/file}}`

- Open a file in the default editor, with the cursor at the end of the file:

`sensible-editor + {{path/to/file}}`

- Open a file in the default editor, with the cursor at the beginning of line 10:

`sensible-editor +10 {{path/to/file}}`

- Open 3 files in vertically split editor windows at the same time:

`sensible-editor -O3 {{path/to/file1 path/to/file2 path/to/file3}}`
