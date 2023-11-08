# sgitopnm

> Convert an SGI file to a PNM file.
> More information: <https://netpbm.sourceforge.net/doc/sgitopnm.html>.

- Convert an SGI image to a PNM file:

`sgitopnm {{path/to/input.sgi}} > {{path/to/output.pnm}}`

- Display information about the SGI file:

`sgitopnm -verbose {{path/to/input.sgi}} > {{path/to/output.pnm}}`

- Extract channel n of the SGI file:

`sgitopnm -channel {{n}} {{path/to/input.sgi}} > {{path/to/output.pnm}}`
