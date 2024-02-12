# pnmmontage

> Create a montage from multiple PNM images.
> More information: <https://netpbm.sourceforge.net/doc/pnmmontage.html>.

- Produce a packing of the specified images:

`pnmmontage {{path/to/image1.pnm path/to/image2.pnm ...}} > {{path/to/output.pnm}}`

- Specify the quality of the packing (Note: larger values produce smaller packings but take longer to compute.):

`pnmmontage -{{0..9}} {{path/to/image1.pnm path/to/image2.pnm ...}} > {{path/to/output.pnm}}`

- Produce a packing that is not larger than `p` percent of the optimal packing:

`pnmmontage -quality {{p}} {{path/to/image1.pnm path/to/image2.pnm ...}} > {{path/to/output.pnm}}`

- Write the positions of the input files within the packed image to a machine-readable file:

`pnmmontage -data {{path/to/datafile}} {{path/to/image1.pnm path/to/image2.pnm ...}} > {{path/to/output.pnm}}`
