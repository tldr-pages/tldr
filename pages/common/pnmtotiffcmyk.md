# pnmtotiffcmyk

> Convert a PNM image to a CMYK encoded TIFF.
> More information: <https://netpbm.sourceforge.net/doc/pnmtotiffcmyk.html>.

- Convert a PNM image to a CMYK encoded TIFF:

`pnmtotiffcmyk {{path/to/input_file.pnm}} > {{path/to/output_file.tiff}}`

- Specify the TIFF compression method:

`pnmtotiffcmyk -{{none|packbits|lzw}} {{path/to/input_file.pnm}} > {{path/to/output_file.tiff}}`

- Control the fill order:

`pnmtotiffcmyk -{{msb2lsb|lsb2msb}} {{path/to/input_file.pnm}} > {{path/to/output_file.tiff}}`
