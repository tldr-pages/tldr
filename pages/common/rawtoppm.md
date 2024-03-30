# rawtoppm

> Convert a raw RGB stream to a PPM image.
> More information: <https://netpbm.sourceforge.net/doc/rawtoppm.html>.

- Convert a raw RGB stream to a PPM image:

`rawtoppm {{width}} {{height}} {{path/to/image.raw}} > {{path/to/output.ppm}}`

- Convert a raw RGB stream in which the pixels come bottom-first instead of top-first to a PPM image:

`rawtoppm {{width}} {{height}} {{path/to/image.raw}} | pamflip -tb > {{path/to/output.ppm}}`

- Ignore the first n bytes of the specified file:

`rawtoppm {{width}} {{height}} -headerskip {{n}} {{path/to/image.raw}} > {{path/to/output.ppm}}`

- Ignore the last m bytes of each row in the specified file:

`rawtoppm {{width}} {{height}} -rowskip {{m}} {{path/to/image.raw}} > {{path/to/output.ppm}}`

- Specify the order of color components for each pixel:

`rawtoppm {{width}} {{height}} -{{rgb|rbg|grb|gbr|brg|bgr}} {{path/to/image.raw}} > {{path/to/output.ppm}}`
