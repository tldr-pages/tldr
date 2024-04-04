# gunzip

> Extract files from a `gzip` (`.gz`) archive.
> More information: <https://manned.org/gunzip>.

- Extract a file from an archive, replacing the original file if it exists:

`gunzip {{archive.tar.gz}}`

- Extract a file to a target destination:

`gunzip --stdout {{archive.tar.gz}} > {{archive.tar}}`

- Extract a file and keep the archive file:

`gunzip --keep {{archive.tar.gz}}`

- List the contents of a compressed file:

`gunzip --list {{file.txt.gz}}`

- Decompress an archive from `stdin`:

`cat {{path/to/archive.gz}} | gunzip`
