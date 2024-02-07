# pnmcrop

> Crop PNM images.
> More information: <https://netpbm.sourceforge.net/doc/pnmcrop.html>.

- Remove white borders on a PNM image:

`pnmcrop -white {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Remove borders of the specified color that are on the top and left side of the image:

`pnmcrop -bg-color {{color}} -top -left {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Determine the color of the borders to be removed by the color of the pixel in the specified corner:

`pnmcrop -bg-corner {{topleft|topright|bottomleft|bottomright}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Leave a border with a width of `n` pixels. Additionally, specify the behaviour if the image is entirely made out of background:

`pnmcrop -margins {{n}} -blank-image {{pass|minimize|maxcrop}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`
