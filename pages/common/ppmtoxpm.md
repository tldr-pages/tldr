# ppmtoxpm

> Convert a PPM image to an X11 version 3 pixmap.
> More information: <https://netpbm.sourceforge.net/doc/ppmtoxpm.html>.

- Convert a PPM image to a XPM image:

`ppmtoxpm {{path/to/input_file.ppm}} > {{path/to/output_file.xpm}}`

- Specify the prefix string in the output XPM image:

`ppmtoxpm -name {{prefix_string}} {{path/to/input_file.ppm}} > {{path/to/output_file.xpm}}`

- In the output XPM file, specify colors by their hexadecimal code instead of their name:

`ppmtoxpm -hexonly {{path/to/input_file.ppm}} > {{path/to/output_file.xpm}}`

- Use the specified PGM file as a transparency mask:

`ppmtoxpm -alphamask {{path/to/alpha_file.pgm}} {{path/to/input_file.ppm}} > {{path/to/output_file.xpm}}`
