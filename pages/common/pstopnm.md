# pstopnm

> Convert a PostScript file to a PNM image.
> More information: <https://netpbm.sourceforge.net/doc/pstopnm.html>.

- Convert a PS file to PNM images, storing page N of the input to `path/to/fileN.ppm`:

`pstopnm {{path/to/file.ps}}`

- Explicitly specify the output format:

`pstopnm -{{pbm|pgm|ppm}} {{path/to/file.ps}}`

- Specify the resolution of the output in dots per inch:

`pstopnm -dpi {{n}} {{path/to/file.ps}}`
