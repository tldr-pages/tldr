# pgmramp

> Generate a greyscale map.
> More information: <https://netpbm.sourceforge.net/doc/pgmramp.html>.

- Generate a left-to-right greyscale map:

`pgmramp -lr > {{path/to/output.pgm}}`

- Generate a top-to-bottom greyscale map:

`pgmramp -tb > {{path/to/output.pgm}}`

- Generate a rectangular greyscale map:

`pgmramp -rectangle > {{path/to/output.pgm}}`

- Generate a elliptical greyscale map:

`pgmramp -ellipse {{path/to/image.pgm}} > {{path/to/output.pgm}}`

- Generate a greyscale map from the top-left corner to the bottom-right corner:

`pgmramp -diagonal {{path/to/image.pgm}} > {{path/to/output.pgm}}`
