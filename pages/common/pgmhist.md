# pgmhist

> Print a histogram of the values present in a PGM image.
> See also: `ppmhist`.
> More information: <https://netpbm.sourceforge.net/doc/pgmhist.html>.

- Display the histogram for human reading:

`pgmhist {{path/to/image.pgm}}`

- Display the median grey value:

`pgmhist {{[-me|-median]}} {{path/to/image.pgm}}`

- Display the four quartile grey values:

`pgmhist {{[-qua|-quartile]}} {{path/to/image.pgm}}`

- Report the existence of invalid grey values:

`pgmhist {{[-f|-forensic]}} {{path/to/image.pgm}}`

- Display machine-readable output:

`pgmhist {{[-ma|-machine]}} {{path/to/image.pgm}}`
