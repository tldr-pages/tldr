# pamcut

> Cut out a rectangular region from a Netpbm image.
> See also: `pamcrop`, `pamdice`, `pamcomp`.
> More information: <https://netpbm.sourceforge.net/doc/pamcut.html>.

- Discard the specified number of columns/rows on each side of the image:

`pamcut {{[-cropl|-cropleft]}} {{value}} {{[-cropr|-cropright]}} {{value}} {{[-cropt|-croptop]}} {{value}} {{[-cropb|-cropbottom]}} {{value}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- Keep only the columns between the specified columns (inclusively):

`pamcut {{[-l|-left]}} {{value}} {{[-ri|-right]}} {{value}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- Fill missing areas with black pixels if the specified rectangle does not entirely lie within the input image:

`pamcut {{[-t|-top]}} {{value}} {{[-b|-bottom]}} {{value}} -pad {{path/to/image.ppm}} > {{path/to/output.ppm}}`
