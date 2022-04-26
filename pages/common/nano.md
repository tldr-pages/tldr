# nano

> Edit files in a terminale.
> More information: <https://nano-editor.org>.

- Start the editor:

`nano`

- Start the editor without loading startup configs:

`nano --ignorercfiles`

- Open specific files:

`nano {{path/to/file1 path/to/file2 ...}}`

- Open a file and position the cursor at a specific line and column:

`nano +{{line}},{{column}} {{path/to/file}}`

- Open a file and enable soft wrapping:

`nano --softwrap {{path/to/file}}`

- Open a file and indent new lines to the previous line indentation:

`nano --autoindent {{path/to/file}}`

- Open a file and create a backup file (`path/to/file~`) on save:

`nano --backup {{path/to/file}}`
