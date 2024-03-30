# pnmtorle

> Convert a PNM file to an Utah Raster Tools RLE image file.
> More information: <https://netpbm.sourceforge.net/doc/pnmtorle.html>.

- Convert a PNM image to an RLE image:

`pnmtorle {{path/to/input.pnm}} > {{path/to/output.rle}}`

- Print PNM header information to `stdout`:

`pnmtorle -verbose {{path/to/input.pnm}} > {{path/to/output.rle}}`

- Include a transparency channel in the output image in which every black pixel is set to fully transparent and every other pixel is set to fully opaque:

`pnmtorle -alpha {{path/to/input.pnm}} > {{path/to/output.rle}}`
