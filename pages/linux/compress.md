# compress

> Compress files using the Unix `compress` command.
> More information: <https://www.unix.com/man-page/osx/1/compress/>.

- Compress specific files:

`compress {{path/to/file1 path/to/file2 ...}}`

- Compress specific files, ignore non-existent ones:

`compress -force {{path/to/file}}`

- Set maximum compression bits (9-16 bits):

`compress -b`

- Write to standard output (no files are changed):

`compress -c {{path/to/file}}`

- Decompress files (functions like `uncompress`):

`compress -d {{path/to/file}}`

- Omit compressed file header:

`compress -n {{path/to/file}}`

- Display compression percentage:

`compress -v {{path/to/file}}`
