# pnmsmooth

> Smooth out a PNM image.
> More information: <https://netpbm.sourceforge.net/doc/pnmsmooth.html>.

- Smooth out a PNM image using a convolution matrix of size 3x3:

`pnmsmooth {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Smooth out a PNM image using a convolution matrix of size width times height:

`pnmsmooth {{[-w|-width]}} {{width}} {{[-h|-height]}} {{height}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`
