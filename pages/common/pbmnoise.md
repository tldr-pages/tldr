# pbmnoise

> Generate white noise.
> More information: <https://netpbm.sourceforge.net/doc/pbmnoise.html>.

- Generate a PGM image containing white noise:

`pbmnoise {{width}} {{height}} > {{path/to/output.pbm}}`

- Specify the seed for the pseudo-random number generator:

`pbmnoise {{width}} {{height}} -randomseed {{value}} > {{path/to/output.pbm}}`

- Specify the desired rate of white to black pixels:

`pbmnoise {{width}} {{height}} -ratio {{1/3}} > {{path/to/output.pbm}}`
