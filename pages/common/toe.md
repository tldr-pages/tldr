# toe

> List terminal types and their descriptions from the terminfo database.
> See also: `infocmp`, `tic`.
> More information: <https://manned.org/toe>.

- List entries from the first terminal database directory found (usually `/usr/share/terminfo`):

`toe`

- List entries from all terminal database directories:

`toe -a`

- Sort entries by name and identify the terminal database they belong to:

`toe -a -s`

- List entries from a specific directory:

`toe {{path/to/terminfo_directory}}`

- Display each terminal database directory as it is accessed:

`toe -h`

- Display version:

`toe -V`
