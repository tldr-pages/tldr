# sldtoppm

> Convert an AutoCAD slide file to a PPM image.
> More information: <https://netpbm.sourceforge.net/doc/sldtoppm.html>.

- Convert an SLD file to a PPM image:

`sldtoppm {{path/to/input.sld}} > {{path/to/output.ppm}}`

- Compensate for non-square pixels by scaling the width of the image:

`sldtoppm -adjust {{path/to/input.sld}} > {{path/to/output.ppm}}`
