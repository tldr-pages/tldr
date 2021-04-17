# gunzip

> Extract file(s) from a gzip (.gz) archive.
> More information: <https://manned.org/gunzip>.

- Extract a file from an archive, replacing the original file if it exists:

`gunzip {{archive.tar.gz}}`

- Extract a file to a target destination:

`gunzip -c {{archive.tar.gz}} > {{archive.tar}}`

- List the contents of a compressed file:

`gunzip -l {{file.txt.gz}}`
