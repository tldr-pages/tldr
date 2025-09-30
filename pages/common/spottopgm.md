# spottopgm

> Convert a SPOT satellite image to PGM format.
> More information: <https://netpbm.sourceforge.net/doc/spottopgm.html>.

- Convert the specified SPOT image to PGM format:

`spottopgm {{path/to/file.spot}} > {{path/to/output.pgm}}`

- Extract the specified color channel:

`spottopgm -{{1|2|3}} {{path/to/file.spot}} > {{path/to/output.pgm}}`

- Extract the specified rectangle from the input image:

`spottopgm {{first_col first_row last_col last_row}} {{path/to/file.spot}} > {{path/to/output.pgm}}`
