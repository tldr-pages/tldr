# pnmindex

> Build a visual index of multiple PNM images.
> See also: `pamundice`.
> More information: <https://netpbm.sourceforge.net/doc/pnmindex.html>.

- Produce an image containing thumbnails of the specified images in a grid:

`pnmindex {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pnm}}`

- Specify the size of the (quadratic) thumbnails:

`pnmindex {{[-s|-size]}} {{50}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pnm}}`

- Specify the number of thumbnails per row:

`pnmindex {{[-a|-across]}} {{10}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pnm}}`

- Specify the maximum number of colors in the output:

`pnmindex {{[-c|-colors]}} {{512}} {{path/to/input1.pnm path/to/input2.pnm ...}} > {{path/to/output.pnm}}`
