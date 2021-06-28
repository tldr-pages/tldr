# jtbl

> Utility to print JSON and JSON Lines data as a table in the terminal.
> More information: <https://github.com/kellyjonbrazil/jtbl>.

- Print a table from JSON input:

`cat {{file.json}} | jtbl`

- Specify the column width for wrapping:

`cat {{file.json}} | jtbl --cols={{number}}`

- Truncate rows instead of wrapping:

`cat {{file.json}} | jtbl -t`

- No wrapping or truncation of rows:

`cat {{file.json}} | jtbl -n`
