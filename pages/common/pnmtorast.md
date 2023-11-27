# pnmtorast

> Convert a PNM file to a Sun rasterfile.
> More information: <https://netpbm.sourceforge.net/doc/pnmtorast.html>.

- Convert a PNM image to a RAST image:

`pnmtorast {{path/to/input.pnm}} > {{path/to/output.rast}}`

- Force either `RT_STANDARD` or `RT_BYTE_ENCODED` form for the output:

`pnmtorast -{{standard|rle}} {{path/to/input.pnm}} > {{path/to/output.rast}}`
