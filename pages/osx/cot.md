# cot

> The Plain-Text Editor for macOS.
> More information: <https://coteditor.com/>.

- Start CotEditor:

`cot`

- Open a new blank document:

`cot --new`

- Open specific files:

`cot {{path/to/file1 path/to/file2 ...}}`

- Open a specific file in the foreground (blocking the terminal until the editor is closed):

`cot --wait {{path/to/file}}`

- Open a specific file with the cursor at a specific line and column:

`cot --line {{line_number}} --column {{column_number}} {{path/to/file}}`
