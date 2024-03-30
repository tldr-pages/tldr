# palmtopnm

> Convert a Palm bitmap file to a PNM image.
> More information: <https://netpbm.sourceforge.net/doc/palmtopnm.html>.

- Convert a Palm bitmap to a PNM image:

`palmtopnm {{path/to/file.palm}} > {{path/to/file.pnm}}`

- Display information about the input file:

`palmtopnm -verbose {{path/to/file.palm}} > {{path/to/file.pnm}}`

- Convert the n'th rendition of the image contained in the input file:

`palmtopnm -rendition {{n}} {{path/to/file.palm}} > {{path/to/file.pnm}}`

- Write a histogram of the colors in the input file to `stdout`:

`palmtopnm -showhist {{path/to/file.palm}} > {{path/to/file.pnm}}`

- Output the transparent color of the input image if set:

`palmtopnm -transparent {{path/to/file.palm}}`
