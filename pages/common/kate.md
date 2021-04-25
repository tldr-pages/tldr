# kate

> KDE Text Editor.
> More information: <https://kate-editor.org/>.

- Launch Kate and open specific files:

`kate {{path/to/file1}} {{path/to/file2}}`

- Open a remote document in Kate:

`kate {{https://example.com}}`

- Start a new Kate instance:

`kate --new`

- Open a file in Kate with the cursor at the specific line:

`kate --line {{line_number}} {{path/to/file}}`

- Delete the files opened by Kate after use:

`kate --tempfile`

- Launch Kate creating a file from stdin:

`cat {{path/to/file}} | kate --stdin`

- Display help:

`kate --help`
