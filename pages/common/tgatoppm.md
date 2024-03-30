# tgatoppm

> Convert a TrueVision Targa file to a Netpbm image.
> More information: <https://netpbm.sourceforge.net/doc/tgatoppm.html>.

- Convert a TrueVision Targa file to a PPM image:

`tgatoppm {{path/to/file.tga}} > {{path/to/output.ppm}}`

- Dump information from the TGA header to `stdout`:

`tgatoppm --headerdump {{path/to/file.tga}} > {{path/to/output.ppm}}`

- Write the transparency channel values of the input image to the specified file:

`tgatoppm --alphaout {{path/to/transparency_file.pgm}} {{path/to/file.tga}} > {{path/to/output.ppm}}`

- Display version:

`tgatoppm -version`
