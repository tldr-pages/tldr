# jtbl

> Utility to print JSON and JSON Lines data as a table in the terminal.
> More information: <https://github.com/kellyjonbrazil/jtbl>.

- Print a table from JSON or JSON Lines input:

`cat {{path/to/file.json}} | jtbl`

- Print a table and specify the column width for wrapping:

`cat {{path/to/file.json}} | jtbl --cols={{width}}`

- Print a table and truncate rows instead of wrapping:

`cat {{path/to/file.json}} | jtbl -t`

- Print a table and don't wrap or truncate rows:

`cat {{path/to/file.json}} | jtbl -n`
