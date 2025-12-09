# pnmtops

> Convert a PNM image to a PostScript file.
> More information: <https://netpbm.sourceforge.net/doc/pnmtops.html>.

- Convert a PNM image to a PS file:

`pnmtops {{path/to/file.pnm}} > {{path/to/file.ps}}`

- Specify the dimensions of the output image in inches:

`pnmtops {{[-imagew|-imagewidth]}} {{imagewidth}} {{[-imageh|-imageheight]}} {{imageheight}} {{path/to/file.pnm}} > {{path/to/file.ps}}`

- Specify the dimensions of the page the output image resides on in inches:

`pnmtops {{[-w|-width]}} {{width}} {{[-h|-height]}} {{height}} {{path/to/file.pnm}} > {{path/to/file.ps}}`
