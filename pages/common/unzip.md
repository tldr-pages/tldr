# unzip

> Extract compressed files/directories from zip archives.
> See also: `zip`.
> More information: <https://manned.org/unzip>.

- Extract files/directories from specific archives:

`unzip {{path/to/archive1 path/to/archive2 ...}}`

- Extract files/directories from archives to a specific path:

`unzip {{path/to/archive1 path/to/archive2 ...}} -d {{path/to/output}}`

- Extract files/directories from archives to stdout alongside extracted file/directory names:

`unzip -c {{path/to/archive1 path/to/archive2 ...}}`

- Extract files/directories from archives created on Windows containing files/directories with non-ASCII (e.g. Chinese or Japanese characters) names:

`unzip -O {{gbk}} {{path/to/archive1 path/to/archive2 ...}}`

- Print contents of a specific archive:

`unzip -l {{path/to/archive.zip}}`
