# pamditherbw

> Apply dithering to a greyscale image, i.e. turn it into a pattern of black and white pixels that look the same as the original greyscale.
> See also: `pbmreduce`.
> More information: <https://netpbm.sourceforge.net/doc/pamditherbw.html>.

- Read a PGM image, apply dithering and save it to a file:

`ppmditherbw {{path/to/image.pgm}} > {{path/to/file.pgm}}`

- Use the specified quantization method:

`ppmditherbw -{{floyd|fs|atkinson|threshold|hilbert|...}} {{path/to/image.pgm}} > {{path/to/file.pgm}}`

- Use the atkinson quantization method and the specified seed for a pseudo-random number generator:

`ppmditherbw -atkinson -randomseed {{1337}} {{path/to/image.pgm}} > {{path/to/file.pgm}}`

- Specify the thresholding value for quantization methods that perform some sort of thresholding:

`ppmditherbw -{{fs|atkinson|thresholding}} -value {{0.3}} {{path/to/image.pgm}} > {{path/to/file.pgm}}`
