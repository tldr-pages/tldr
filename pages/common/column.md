# column

> Format text into multiple columns or aligned tables.
> More information: <https://man.openbsd.org/column>.

- Format a list into columns that fit the terminal width:

`column {{path/to/file}}`

- Align whitespace-separated fields in a [t]able:

`column -t {{path/to/file}}`

- Align fields in a [t]able, using a comma as the [s]eparator:

`column -t -s , {{path/to/file}}`

- Format a list for a display with a specific width in [c]olumns:

`column -c {{80}} {{path/to/file}}`

- Fill rows before columns, using a specific display width:

`column -x -c {{80}} {{path/to/file}}`
