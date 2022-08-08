# unzip

> Extract compressed files/directories from zip archives.
> See also: `zip`.
> More information: <https://manned.org/unzip>.

- Extract all files/directories from specific archives into the current directory:

`unzip {{path/to/archive1 path/to/archive2 ...}}`

- Extract files/directories from archives to a specific path:

`unzip {{path/to/archive1 path/to/archive2 ...}} -d {{path/to/output}}`

- Extract files/directories from archives to `stdout`:

`unzip -c {{path/to/archive1 path/to/archive2 ...}}`

- Extract files/directories from archives created on Windows containing non-ASCII file names:

`unzip -O {{gbk}} {{path/to/archive1 path/to/archive2 ...}}`

- List the contents of a specific archive without extracting them:

`unzip -l {{path/to/archive.zip}}`
