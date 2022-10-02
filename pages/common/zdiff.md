# zdiff

> Invoke `diff` on gzipped files.
> More information: <https://manned.org/zdiff>.

- Compare two files, uncompressing them if necessary:

`zdiff {{path/to/file1.gz}} {{path/to/file2.gz}}`

- Invoke `diff` on `path/to/file.txt` and `path/to/file.txt.gz` (which is assumed to exist):

`zdiff {{path/to/file.txt}}`
