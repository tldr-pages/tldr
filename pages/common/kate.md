# kate

> KDE's advanced text editor.
> More information: <https://kate-editor.org/>.

- Open specific files:

`kate {{path/to/file1 path/to/file2 ...}}`

- Open specific remote files:

`kate {{https://example.com/path/to/file1 https://example.com/path/to/file2 ...}}`

- Create a new editor instance even if one is already open:

`kate --new`

- Open a file with the cursor at the specific line:

`kate --line {{line_number}} {{path/to/file}}`

- Open a file with the cursor at the specific line and column:

`kate --line {{line_number}} --column {{column_number}} {{path/to/file}}`

- Create a file from `stdin`:

`cat {{path/to/file}} | kate --stdin`

- Display help:

`kate --help`
