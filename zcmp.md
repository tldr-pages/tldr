# zcmp

> Invoke `cmp` on gzip compressed files.
> More information: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Compare two files, uncompressing then if necessary:

`zcmp {{file1.txt.gz}} {{file2.txt.gz}}`

- Compare a file to its compressed version (assumed to have a `.gz` extension):

`zcmp {{file.txt}}`
