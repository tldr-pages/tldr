# ppmdist

> Produce a grayscale version of a PPM image.
> More information: <https://netpbm.sourceforge.net/doc/ppmdist.html>.

- Produce a grayscale version of the specified PPM image:

`ppmdist {{path/to/input.ppm}} > {{path/to/output.pgm}}`

- Use the specified method to map colors to graylevels:

`ppmdist -{{frequency|intensity}} {{path/to/input.ppm}} > {{path/to/output.pgm}}`
