# unzip

> Extract files/directories from ZIP archives.
> See also: `zip`.
> More information: <https://manned.org/unzip>.

- Extract all files/directories from specific archives into the current directory:

`unzip {{path/to/archive1.zip path/to/archive2.zip ...}}`

- Extract files/directories from archives to a specific path:

`unzip {{path/to/archive1.zip path/to/archive2.zip ...}} -d {{path/to/output}}`

- Extract files/directories from archives to `stdout`:

`unzip -c {{path/to/archive1.zip path/to/archive2.zip ...}}`

- Extract the contents of the file(s) to `stdout` alongside the extracted file names:

`unzip -O {{gbk}} {{path/to/archive1.zip path/to/archive2.zip ...}}`

- List the contents of a specific archive without extracting them:

`unzip -l {{path/to/archive.zip}}`

- Extract a specific file from an archive:

`unzip -j {{path/to/archive.zip}} {{path/to/file_in_archive1 path/to/file_in_archive2 ...}}`
