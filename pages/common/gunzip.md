# gunzip

> Extract file(s) from a gzip (.gz) archive.

- Extract a file from the archive replacing the original file:

`gunzip {{archive.tar.gz}}`

- Extract file to a target destination:

`gunzip -c {{archive.tar.gz}} > {{archive.tar}}`

- List of contents of the compressed file:

`gunzip -l {{file.txt.gz}}`
