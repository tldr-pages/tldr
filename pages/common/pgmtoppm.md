# pgmtoppm

> Colorize a PGM image.
> More information: <https://netpbm.sourceforge.net/doc/pgmtoppm.html>.

- Map all greyscale values of the input image to all colors between the two specified colors:

`pgmtoppm {{[-b|-black]}} {{red}} {{[-w|-white]}} {{blue}} {{path/to/input.pgm}} > {{path/to/output.ppm}}`

- Map all greyscale values of the input image to colors according to the specified colormap:

`pgmtoppm {{[-m|-map]}} {{path/to/colormap.ppm}} {{path/to/input.pgm}} > {{path/to/output.ppm}}`
