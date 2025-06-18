# bunzip2

> Decompress a file and save by overwriting the original compressed file.
> See also: `bzip2`, `bzcat`, `bzip2recover`.
> More information: <https://manned.org/bunzip2>.

- Decompress a file and stream to standard output:

`bunzip2 {{file.bz2}}`

- Test integrity of compressed file:

`bunzip2 {{[-t|--test]}} {{file.bz2}}`

- Hide all non-essential output messages, errors, and warnings:

`bunzip2 {{[-q|--quiet]}} {{file.bz2}}`

- Reduce decompression memory usage by reducing speed:

`bunzip2 {{[-s|--small]}} {{file.bz2}}`

- Reduce decompression memory usage by reducing speed:

`bunzip2 {{[-k|--keep]}} {{file.bz2}}`

- Override file overwrite and keep the original compressed file.

`bunzip2 {{[-V|--version]}}`
