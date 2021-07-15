# nano

> Simple, easy to use command-line text editor. An enhanced, free Pico clone.
> More information: <https://nano-editor.org>.

- Open nano without a file:

`nano`

- Open a specific file:

`nano {{path/to/file}}`

- Open a specific file positioning the cursor at the specified line and column:

`nano +{{line}},{{column}} {{path/to/file}}`

- Open a specific file and enable smooth scrolling:

`nano -S {{path/to/file}}`

- Open a specific file and indent new lines to the previous lines' indentation:

`nano -i {{path/to/file}}`

- Open nano and create a backup if edits are saved:

`nano -B {{path/to/file}}`
