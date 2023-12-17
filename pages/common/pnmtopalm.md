# pnmtopalm

> Convert a PNM image to a Palm bitmap.
> More information: <https://netpbm.sourceforge.net/doc/pnmtopalm.html>.

- Convert a PNM image to a Palm bitmap:

`pnmtopalm {{path/to/file.pnm}} > {{path/to/file.palm}}`

- Specify the color depth of the resulting bitmap:

`pnmtopalm -depth {{1|2|4|8|16}} {{path/to/file.pnm}} > {{path/to/file.palm}}`

- Choose a compression method for the resulting bitmap:

`pnmtopalm -{{scanline_compression|rle_compression|packbits_compression}} {{path/to/file.pnm}} > {{path/to/file.palm}}`

- Build a custom colormap and include it in the resulting bitmap:

`pnmtopalm -colormap {{path/to/file.pnm}} > {{path/to/file.palm}}`

- Specify the bitmap's density:

`pnmtopalm -density {{72|108|144|216|288}} {{path/to/file.pnm}} > {{path/to/file.palm}}`
