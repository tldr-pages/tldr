# picttoppm

> Convert a Macintosh PICT file to a PPM image.
> More information: <https://netpbm.sourceforge.net/doc/picttoppm.html>.

- Convert a PICT file to a PPM image:

`picttoppm {{path/to/file.pict}} > {{path/to/file.ppm}}`

- Force any images in the PICT file to be output at full resolution:

`picttoppm -fullres {{path/to/file.pict}} > {{path/to/file.ppm}}`

- Do not assume that the input file contains a PICT header and execute quickdraw operations only:

`picttoppm -noheader -quickdraw {{path/to/file.pict}} > {{path/to/file.ppm}}`
