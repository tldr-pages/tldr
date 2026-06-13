# pgmnoise

> Generate white noise.
> More information: <https://netpbm.sourceforge.net/doc/pgmnoise.html>.

- Generate a PGM image containing white noise:

`pgmnoise {{width}} {{height}} > {{path/to/output.pgm}}`

- Specify the seed for the pseudo-random number generator:

`pgmnoise {{width}} {{height}} -randomseed {{value}} > {{path/to/output.pgm}}`
