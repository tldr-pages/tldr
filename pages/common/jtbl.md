# jtbl

> Utility to print JSON and JSON Lines data as a table in the terminal.
> More information: <https://github.com/kellyjonbrazil/jtbl>.

- Print a table from JSON or JSON Lines input:

`jtbl < {{file.json}}`

- Print a table and specify the column width for wrapping:

`jtbl --cols={{width}} < {{file.json}}`

- Print a table and truncate rows instead of wrapping:

`jtbl {{[-t|--truncate]}} < {{file.json}}`

- Print a table and don't wrap or truncate rows:

`jtbl {{[-n|--no-wrap]}} < {{file.json}}`
