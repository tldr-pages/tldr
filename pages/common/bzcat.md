# bzcat

> Decompress files to standard output.
> See also: `bzip2`, `bunzip2`, `bzip2recover`.
> More information: <https://manned.org/bzcat>.

- Decompress a file and stream to standard output:

`bzcat {{file.bz2}}`

- Test integrity of compressed file:

`bzcat {{[-t|--test]}} {{file.bz2}}`

- Hide all non-essential output messages, errors, and warnings:

`bzcat {{[-q|--quiet]}} {{file.bz2}}`

- Reduce decompression memory usage by reducing speed:

`bzcat {{[-s|--small]}} {{file.bz2}}`

- Display version number of bzcat:

`bzcat {{[-V|--version]}}`
