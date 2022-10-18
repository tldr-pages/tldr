# bzip2

> Compress (bzip2) or decompress (bunzip2) files. Decompress files to stdout (bzcat) and recover data from damaged bzip2 files (bzip2recover.).
> More information: <https://ss64.com/osx/bzip.html>.

- Force decompression:

`bzip2 -d {{filename}}`

- Test compressed file integrity:

`bzip2 -t {{filename}}`

- Verbose mode -- show the compression ratio for each file processed:

`bzip2 -v {{filename}}`

- Print help:

`bzip2 -h`

- Overwrite existing output files:

`bzip2 -f {{filename}}`
