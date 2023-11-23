# ximtoppm

> Convert a XIM file to a PPM image.
> More information: <https://netpbm.sourceforge.net/doc/ximtoppm.html>.

- Convert an XIM image to a PPM image:

`ximtoppm {{path/to/input_file.xim}} > {{path/to/output_file.ppm}}`

- Store the transparency mask of the input image in the specified file:

`ximtoppm --alphaout {{path/to/alpha_file.pbm}} {{path/to/input_file.xim}} > {{path/to/output_file.ppm}}`
