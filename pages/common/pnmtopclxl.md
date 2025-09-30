# pnmtopclxl

> Convert a PNM file to an HP LaserJet PCL XL printer stream.
> More information: <https://netpbm.sourceforge.net/doc/pnmtopclxl.html>.

- Convert PNM files to an HP LaserJet PCL XL printer stream:

`pnmtopclxl {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pclxl}}`

- Specify the resolution of the image as well as the location of the page from the upper left corner of each image:

`pnmtopclxl -dpi {{resolution}} {{[-x|-xoffs]}} {{x_offset}} {{[-y|-yoffs]}} {{y_offset}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pclxl}}`

- Generate a duplex printer stream for the specified paper format:

`pnmtopclxl {{[-du|-duplex]}} {{vertical|horizontal}} {{[-fo|-format]}} {{letter|legal|a3|a4|a5|...}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pclxl}}`
