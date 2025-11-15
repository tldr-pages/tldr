# rawtopgm

> Convert a raw greyscale image to a PGM image.
> More information: <https://netpbm.sourceforge.net/doc/rawtopgm.html>.

- Convert a raw greyscale image to a PGM image:

`rawtopgm {{width}} {{height}} {{path/to/image.raw}} > {{path/to/output.pgm}}`

- Convert a raw greyscale image to a PGM image, assume the image to be a square:

`rawtopgm {{path/to/image.raw}} > {{path/to/output.pgm}}`

- Convert a raw greyscale image in which the pixels come bottom-first instead of top-first to a PGM image:

`rawtopgm {{width}} {{height}} {{[-bt|-bottomfirst]}} {{path/to/image.raw}} > {{path/to/output.pgm}}`

- Ignore the first `n` bytes of the specified file:

`rawtopgm {{width}} {{height}} {{[-h|-headerskip]}} {{n}} {{path/to/image.raw}} > {{path/to/output.pgm}}`

- Ignore the last m bytes of each row in the specified file:

`rawtopgm {{width}} {{height}} {{[-r|-rowskip]}} {{m}} {{path/to/image.raw}} > {{path/to/output.pgm}}`

- Specify the maxval for the grey values in the input to be equal to `n`:

`rawtopgm {{width}} {{height}} {{[-m|-maxval]}} {{n}} {{path/to/image.raw}} > {{path/to/output.pgm}}`

- Specify the number of bytes that represent each sample in the input and that the byte-sequence is to be interpreted as little-endian:

`rawtopgm {{width}} {{height}} -bpp {{1|2}} {{[-l|-littleendian]}} {{path/to/image.raw}} > {{path/to/output.pgm}}`
