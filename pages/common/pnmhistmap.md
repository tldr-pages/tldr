# pnmhistmap

> Draw a histogram of a PNM image.
> More information: <https://netpbm.sourceforge.net/doc/pnmhistmap.html>.

- Draw a histogram of a PNM image:

`pnmhistmap {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Draw the histogram as dots instead of bars:

`pnmhistmap -dots {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Specify the range of intensity values to include:

`pnmhistmap -lval {{minval}} -rval {{maxval}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`
