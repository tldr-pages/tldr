# engrampa

> Package files into zip/tar file in MATE desktop environment.
> See also: `zip`, `tar`.
> More information: <https://github.com/mate-desktop/engrampa>.

- Start Engrampa:

`engrampa`

- Open specific archives:

`engrampa {{path/to/archive1.tar path/to/archive2.tar ...}}`

- Archive specific files and/or directories recursively:

`engrampa --add-to={{path/to/compressed.tar}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Extract files and/or directories from archives to a specific path:

`engrampa --extract-to={{path/to/directory}} {{path/to/archive1.tar path/to/archive2.tar ...}}`
