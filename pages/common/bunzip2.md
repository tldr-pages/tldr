# bunzip2

> Decompresses a file and saves by overwriting the original compressed file.
> See also: `bzip2`, `bzcat`, `bzip2recover`.
> More information: <https://manned.org/bunzip2>.

- Decompress a file and stream to standard output:

`bzcat {{file.bz2}}`

- Test integrity of compressed file:

`bzcat {{[-t|--test]}} {{file.bz2}}`

- Hide all non-essential output messages, errors, and warnings:

`bzcat {{[-q|--quiet]}} {{file.bz2}}`

- Reduce decompression memory usage by reducing speed:

`bzcat {{[-s|--small]}} {{file.bz2}}`

- Reduce decompression memory usage by reducing speed:

`bzcat {{[-k|--keep]}} {{file.bz2}}`

- Override file overwrite and keep the original compressed file.

`bzcat {{[-V|--version]}}`
