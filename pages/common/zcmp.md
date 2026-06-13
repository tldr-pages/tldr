# zcmp

> Compare compressed files.
> More information: <https://manned.org/zcmp>.

- Invoke `cmp` on two files compressed via `gzip`:

`zcmp {{path/to/file1.gz}} {{path/to/file2.gz}}`

- Compare a file to its gzipped version (assuming `.gz` exists already):

`zcmp {{path/to/file}}`
