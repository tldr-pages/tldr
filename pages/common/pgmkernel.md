# pgmkernel

> Generate a convolution kernel to be used with `pnmconvol`.
> See also: `pnmconvol`.
> More information: <https://netpbm.sourceforge.net/doc/pgmkernel.html>.

- Generate a convolution kernel:

`pgmkernel {{width}} {{height}} > {{path/to/output.pgm}}`

- Generate a quadratic convolution kernel:

`pgmkernel {{size}} > {{path/to/output.pgm}}`

- Specify the weight of the center in the generated kernel:

`pgmkernel -weight {{value}} {{width}} {{height}} > {{path/to/output.pgm}}`
