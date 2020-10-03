# nano

> Simple, easy to use command-line text editor. An enhanced, free Pico clone.
> More information: <https://nano-editor.org>.

- Open a specific file:

`nano {{path/to/file}}`

- Open a file positioning the cursor at the specified line and column:

`nano +{{line}},{{column}} {{path/to/file}}`

- Enable smooth scrolling:

`nano -S {{filename}}`

- Indent new lines to the previous lines' indentation:

`nano -i {{filename}}`

- Before modification, backup separately as `{{current_file_name}}~`:

`nano -B {{filename}}`
