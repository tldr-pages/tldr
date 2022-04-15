# engrampa

> Package files into zip/tar file.
> See also: `zip`, `tar`.
> More information: <https://github.com/mate-desktop/engrampa>.

- Start the archive manager:

`engrampa`

- Open specific archives:

`engrampa {{path/to/archive1.tar path/to/archive2.tar ...}}`

- Archive specific files/directories recursively:

`engrampa --add-to={{path/to/compressed.tar}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Extract files/directories from archives to a specific path:

`engrampa --extract-to={{path/to/directory}} {{path/to/archive1.tar path/to/archive2.tar ...}}`
