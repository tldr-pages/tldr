# ilbmtoppm

> Convert an ILBM file to a PPM image.
> More information: <https://netpbm.sourceforge.net/doc/ilbmtoppm.html>.

- Convert an ILBM file to a PPM image:

`ilbmtoppm {{path/to/file.ilbm}} > {{path/to/file.ppm}}`

- Use the specified color to "show through" where the image is transparent:

`ilbmtoppm {{[-t|-transparent]}} {{color}} {{path/to/file.ilbm}} > {{path/to/file.ppm}}`

- Ignore the chunk with the specified chunk ID:

`ilbmtoppm {{[-ig|-ignore]}} {{chunkID}} {{path/to/file.ilbm}} > {{path/to/file.ppm}}`

- Store the input's transparency information to the specified PBM file:

`ilbmtoppm {{[-m|-maskfile]}} {{path/to/maskfile.pbm}} {{path/to/file.ilbm}} > {{path/to/file.ppm}}`
