# mate

> General-purpose text editor for macOS.
> More information: <https://macromates.com/textmate/manual/opening-files#mate>.

- Start TextMate:

`mate`

- Open specific files:

`mate {{path/to/file1 path/to/file2 ...}}`

- Specify the filetype of a file:

`mate {{[-t|--type]}} {{filetype}} {{path/to/file}}`

- Open and wait until finished editing a specific file:

`mate {{[-w|--wait]}} {{path/to/file}}`

- Open a file with the cursor at a specific line and column:

`mate {{[-l|--line]}} {{line_number}}:{{column_number}} {{path/to/file}}`
