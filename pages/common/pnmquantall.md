# pnmquantall

> Run `pnmquant` on multiple files at once such that they share a common colormap.
> See also: `pnmquant`.
> More information: <https://netpbm.sourceforge.net/doc/pnmquantall.html>.

- Run `pnmquant` on multiple files with the specified parameters, overwriting the original files:

`pnmquantall {{n_colors}} {{path/to/input1.pnm path/to/input2.pnm ...}}`

- Save the quantised images to files named the same as the input files, but with the specified extension appended:

`pnmquantall -ext {{extension}} {{n_colors}} {{path/to/input1.pnm path/to/input2.pnm ...}}`
