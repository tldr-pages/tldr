# zcmp

> Compare compressed files.
> More information: <https://manned.org/zcmp>.

- Invoke `cmp` on two files compressed via `gzip`:

`zcmp {{path/to/file1.txt.gz}} {{path/to/file2.txt.gz}}`

- Compare a file to its gzipped version (assuming that `path/to/file.txt.gz` exists):

`zcmp {{path/to/file.txt}}`
