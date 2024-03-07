# pamcut

> Cut out a rectangular region from a Netpbm image.
> See also: `pamcrop`, `pamdice`, `pamcomp`.
> More information: <https://netpbm.sourceforge.net/doc/pamcut.html>.

- Discard the specified number of columns/rows on each side of the image:

`pamcut -cropleft {{value}} -cropright {{value}} -croptop {{value}} -cropbottom {{value}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- Keep only the columns between the specified columns (inclusively):

`pamcut -left {{value}} -right {{value}} {{path/to/image.ppm}} > {{path/to/output.ppm}}`

- Fill missing areas with black pixels if the specified rectangle does not entirely lie within the input image:

`pamcut -top {{value}} -bottom {{value}} -pad {{path/to/image.ppm}} > {{path/to/output.ppm}}`
