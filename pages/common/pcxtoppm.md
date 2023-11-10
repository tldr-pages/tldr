# pcxtoppm

> Convert a PCX file to a PPM image.
> More information: <https://netpbm.sourceforge.net/doc/pcxtoppm.html>.

- Convert a PCX file to a PPM image:

`pcxtoppm {{path/to/file.pcx}} > {{path/to/file.ppm}}`

- Use a predefined standard palette even if the PCX file provides one:

`pcxtoppm -stdpalette {{path/to/file.pcx}} > {{path/to/file.ppm}}`

- Print information on the PCX header to `stdout`:

`pcxtoppm -verbose {{path/to/file.pcx}} > {{path/to/file.ppm}}`
