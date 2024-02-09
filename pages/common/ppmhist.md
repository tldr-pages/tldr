# ppmhist

> Print a histogram of the colors present in a PPM image.
> See also: `pgmhist`.
> More information: <https://netpbm.sourceforge.net/doc/ppmhist.html>.

- Generate the histogram for human reading:

`ppmhist -nomap {{path/to/image.ppm}}`

- Generate a PPM file of the colormap for the image, with the color histogram as comments:

`ppmhist -map {{path/to/image.ppm}}`

- Display version:

`ppmhist -version`
