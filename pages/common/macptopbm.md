# macptopbm

> Read a MacPaint file as input and produce a PBM image as output.
> More information: <https://netpbm.sourceforge.net/doc/macptopbm.html>.

- Convert a MacPaint file into a PGM image:

`macptopbm {{path/to/file.mac}}`

- Skip over a specified number of bytes when reading the file:

`macptopbm -extraskip {{N}}`

- Suppress all informational messages:

`macptopbm -quiet`

- Display version:

`macptopbm -version`
