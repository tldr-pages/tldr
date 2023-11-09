# pnmtops

> Convert a PNM image to a PostScript file.
> More information: <https://netpbm.sourceforge.net/doc/pnmtops.html>.

- Convert a PNM image to a PS file:

`pnmtops {{path/to/file.pnm}} > {{path/to/file.ps}}`

- Specify the dimensions of the output image in inches:

`pnmtops -imagewidth {{imagewidth}} -imageheight {{imageheight}} {{path/to/file.pnm}} > {{path/to/file.ps}}`

- Specify the dimensions of the page the output image resides on in inches:

`pnmtops -width {{width}} -height {{height}} {{path/to/file.pnm}} > {{path/to/file.ps}}`
