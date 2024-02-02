# pnmtosgi

> Convert a PNM file to an SGI image file.
> More information: <https://netpbm.sourceforge.net/doc/pnmtosgi.html>.

- Convert a PNM image to an SGI image:

`pnmtosgi {{path/to/input.pnm}} > {{path/to/output.sgi}}`

- Disable or enable compression:

`pnmtosgi -{{verbatim|rle}} {{path/to/input.pnm}} > {{path/to/output.sgi}}`

- Write the specified string into the SGI image header's `imagename` field:

`pnmtosgi -imagename {{string}} {{path/to/input.pnm}} > {{path/to/output.sgi}}`
