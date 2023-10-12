# ppmhist

> Print a histogram of the colors present in a PPM image.
> More information: <https://netpbm.sourceforge.net/doc/ppmhist.html>.
- Generate the histogram for human reading:

`ppmhist -nomap {{path/to/ppmfile}}`

- Generate a PPM file of the colormap for the image, with the color histogram as comments:

`ppmhist -map {{path/to/ppmfile}}`

- Display version:

`ppmhist -version`
