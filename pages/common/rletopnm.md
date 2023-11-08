# rletopnm

> Convert a Utah Raster Tools RLE image file to a PNM file.
> More information: <https://netpbm.sourceforge.net/doc/rletopnm.html>.

- Convert an RLE image to a PNM file:

`rletopnm {{path/to/input.rle}} > {{path/to/output.pnm}}`

- Create a PGM image containing the RLE file's alpha channel:

`rletopnm -alphaout {{path/to/alpha_file.pgm}} {{path/to/input.rle}} > {{path/to/output.pnm}}`

- Operate in verbose mode and print the contents of the RLE header to `stdout`:

`rletopnm -verbose {{path/to/input.rle}} > {{path/to/output.pnm}}`
