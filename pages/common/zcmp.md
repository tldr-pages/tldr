# zcmp

> Invoke `cmp` on gzip compressed files.
> More information: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Compare two files, uncompressing them if necessary:

`zcmp {{path/to/file1.txt.gz}} {{path/to/file2.txt.gz}}`

- Compare a file to its gzip compressed version (assuming that `path/to/file.txt.gz` exists):

`zcmp {{path/to/file.txt}}`
