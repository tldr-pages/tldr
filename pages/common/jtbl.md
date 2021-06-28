# jtbl

> Utility to print JSON and JSON Lines data as a table in the terminal.
> More information: <https://github.com/kellyjonbrazil/jtbl>.

- Print a table from JSON or JSON Lines input:

`cat {{file.json}} | jtbl`

- Specify the column width for wrapping:

`cat {{file.json}} | jtbl --cols={{width}}`

- Truncate rows instead of wrapping:

`cat {{file.json}} | jtbl -t`

- Don't wrap or truncate rows:

`cat {{file.json}} | jtbl -n`
