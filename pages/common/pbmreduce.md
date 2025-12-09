# pbmreduce

> Proportionally reduce a PBM image.
> See also: `pamenlarge`, `pamditherbw`.
> More information: <https://netpbm.sourceforge.net/doc/pbmreduce.html>.

- Reduce the specified image by the specified factor:

`pbmreduce {{n}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`

- Use simple thresholding when reducing:

`pbmreduce {{[-t|-threshold]}} {{n}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`

- Use the specified threshold for all quantizations:

`pbmreduce {{[-va|-value]}} {{0.6}} {{n}} {{path/to/image.pbm}} > {{path/to/output.pbm}}`
