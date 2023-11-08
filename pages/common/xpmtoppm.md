# xpmtoppm

> Convert an X11 pixmap to a PPM image.
> More information: <https://netpbm.sourceforge.net/doc/xpmtoppm.html>.

- Convert an XPM image to a PPM image:

`xpmtoppm {{path/to/input_file.xpm}} > {{path/to/output_file.ppm}}`

- Store the transparency mask of the input image in the specified file:

`xpmtoppm --alphaout {{path/to/alpha_file.pbm}} {{path/to/input_file.xpm}} > {{path/to/output_file.ppm}}`
