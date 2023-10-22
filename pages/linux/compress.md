# compress

> Compress files using the Unix `compress` command.
> More information: <https://manned.org/compress.1>.

- Compress specific files:

`compress {{path/to/file1 path/to/file2 ...}}`

- Compress specific files, ignore non-existent ones:

`compress -f {{path/to/file1 path/to/file2 ...}}`

- Set maximum compression bits (9-16 bits):

`compress -b {{bits}}`

- Write to standard output (no files are changed):

`compress -c {{path/to/file}}`

- Decompress files (functions like `uncompress`):

`compress -d {{path/to/file}}`

- Display compression percentage:

`compress -v {{path/to/file}}`
