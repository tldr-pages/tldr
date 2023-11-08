# tifftopnm

> Convert a TIFF image to a PNM image.
> More information: <https://netpbm.sourceforge.net/doc/tifftopnm.html>.

- Convert a TIFF to a PNM file:

`tifftopnm {{path/to/input_file.tiff}} > {{path/to/output_file.pnm}}`

- Create a PGM file containing the alpha channel of the input image:

`tifftopnm -alphaout {{path/to/alpha_file.pgm}} {{path/to/input_file.tiff}} > {{path/to/output_file.pnm}}`

- Respect the `fillorder` tag in the input TIFF image:

`tifftopnm -respectfillorder {{path/to/input_file.tiff}} > {{path/to/output_file.pnm}}`

- Print TIFF header information to `stderr`:

`tifftopnm -headerdump {{path/to/input_file.tiff}} > {{path/to/output_file.pnm}}`
