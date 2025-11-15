# ppmtoicr

> Convert a PPM image to NCSA ICR format.
> More information: <https://netpbm.sourceforge.net/doc/ppmtoicr.html>.

- Convert a PPM image to a ICR file:

`ppmtoicr {{path/to/file.ppm}} > {{path/to/file.icr}}`

- Display the output in name:

`ppmtoicr {{[-w|-windowname]}} {{name}} {{path/to/file.ppm}} > {{path/to/file.icr}}`

- Expand the image by the specified factor:

`ppmtoicr {{[-e|-expand]}} {{factor}} {{path/to/file.ppm}} > {{path/to/file.icr}}`

- Display the output on the screen with the specified number:

`ppmtoicr {{[-d|-display]}} {{number}} {{path/to/file.ppm}} > {{path/to/file.icr}}`
