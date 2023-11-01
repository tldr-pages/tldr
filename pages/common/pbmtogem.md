# pbmtogem

> Read a PBM image as input and produce a compressed GEM .img file as output.
> `pbmtogem` cannot compress repeated lines.
> More information: <https://netpbm.sourceforge.net/doc/pbmtogem.html>.

- Convert a PBM image into a GEM .img file:

`pbmtogem {{path/to/file.pbm}} > {{path/to/file.img}}`

- Suppress all informational messages:

`pbmtogem -quiet`

- Display version:

`pbmtogem -version`
