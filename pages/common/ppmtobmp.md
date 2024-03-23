# ppmtobmp

> Convert a PPM image to a BMP file.
> More information: <https://netpbm.sourceforge.net/doc/ppmtobmp.html>.

- Convert a PPM image to a BMP file:

`ppmtobmp {{path/to/file.ppm}} > {{path/to/file.bmp}}`

- Explicitly specify whether or not a Windows BMP file or an OS/2 BMP file should be created:

`ppmtobmp -{{windows|os2}} {{path/to/file.ppm}} > {{path/to/file.bmp}}`

- Use a specific number of bits for each pixel:

`ppmtobmp -bbp {{1|4|8|24}} {{path/to/file.ppm}} > {{path/to/file.bmp}}`
