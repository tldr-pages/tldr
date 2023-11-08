# ppmtospu

> Convert a PPM file to an Atari Spectrum 512 image.
> More information: <https://netpbm.sourceforge.net/doc/ppmtospu.html>.

- Convert a PPM file to an Atari Spectrum 512 image:

`ppmtospu {{path/to/input.ppm}} > {{path/to/output.spu}}`

- Use a dithering matrix of the specified size (0 means no dithering):

`ppmtospu -d{{0|2|4}} {{path/to/input.ppm}} > {{path/to/output.spu}}`
