# macptopbm

> Read a MacPaint file as input and produce a PBM image as output.
> See also: `pbmtomacp`.
> More information: <https://netpbm.sourceforge.net/doc/macptopbm.html>.

- Convert a MacPaint file into a PGM image:

`macptopbm {{path/to/file.macp}} > {{path/to/output.pbm}}`

- Skip over a specified number of bytes when reading the file:

`macptopbm -extraskip {{N}} > {{path/to/output.pbm}}`

- Suppress all informational messages:

`macptopbm -quiet > {{path/to/output.pbm}}`

- Display version:

`macptopbm -version`
