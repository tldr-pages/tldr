# pnmconvol

> Convolute a PNM image.
> More information: <https://netpbm.sourceforge.net/doc/pnmconvol.html>.

- Convolve a PNM image with the specified convolution matrix:

`pnmconvol -matrix=-1,3,-1 {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Convolve a PNM image with the convolution matrix in the specified files, one for each layer in the input image:

`pnmconvol -matrixfile {{path/to/matrix1,path/to/matrix2,...}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Convolve a PNM image with the convolution matrix in the specified PNM file:

`pnmconvol {{path/to/matrix.pnm}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Normalize the weights in the convolution matrix such that they add up to one:

`pnmconvol -matrix=-1,3,-1 -normalize {{path/to/image.pnm}} > {{path/to/output.pnm}}`
