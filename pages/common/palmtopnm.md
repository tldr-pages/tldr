# palmtopnm

> Convert a Palm bitmap file to a PNM image.
> More information: <https://netpbm.sourceforge.net/doc/palmtopnm.html>.

- Convert a Palm bitmap to a PNM image:

`palmtopnm {{path/to/file.palm}} > {{path/to/file.pnm}}`

- Display information about the input file:

`palmtopnm {{[-verb|-verbose]}} {{path/to/file.palm}} > {{path/to/file.pnm}}`

- Convert the n'th rendition of the image contained in the input file:

`palmtopnm {{[-r|-rendition]}} {{n}} {{path/to/file.palm}} > {{path/to/file.pnm}}`

- Write a histogram of the colors in the input file to `stdout`:

`palmtopnm {{[-s|-showhist]}} {{path/to/file.palm}} > {{path/to/file.pnm}}`

- Output the transparent color of the input image if set:

`palmtopnm {{[-t|-transparent]}} {{path/to/file.palm}}`
