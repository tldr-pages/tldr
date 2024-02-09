# pgmramp

> Generate a greyscale map.
> More information: <https://netpbm.sourceforge.net/doc/pgmramp.html>.

- Generate a left-to-right greyscale map:

`pgmtexture -lr > {{path/to/output.pgm}}`

- Generate a top-to-bottom greyscale map:

`pgmtexture -tb > {{path/to/output.pgm}}`

- Generate a rectangular greyscale map:

`pgmtexture -rectangle > {{path/to/output.pgm}}`

- Generate a elliptical greyscale map:

`pgmtexture -ellipse {{path/to/image.pgm}} > {{path/to/output.pgm}}`

- Generate a greyscale map from the top-left corner to the bottom-right corner:

`pgmtexture -diagonal {{path/to/image.pgm}} > {{path/to/output.pgm}}`
