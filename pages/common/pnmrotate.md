# pnmrotate

> Rotate a PNM image.
> More information: <https://netpbm.sourceforge.net/doc/pnmrotate.html>.

- Rotate a PNM image by some angle (measured in degrees, counter-clockwise):

`pnmrotate {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Specify the background color exposed by rotating the input image:

`pnmrotate -background {{color}} {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Disable anti-aliasing, improving performance but decreasing quality:

`pnmrotate -noantialias {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`
