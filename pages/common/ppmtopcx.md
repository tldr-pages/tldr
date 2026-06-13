# ppmtopcx

> Convert a PPM image to a PCX file.
> More information: <https://netpbm.sourceforge.net/doc/ppmtopcx.html>.

- Convert a PPM image to a PCX file:

`ppmtopcx {{path/to/file.ppm}} > {{path/to/file.pcx}}`

- Produce a PCX file with the specified color depth:

`ppmtopcx -{{8bit|24bit}} {{path/to/file.ppm}} > {{path/to/file.pcx}}`
