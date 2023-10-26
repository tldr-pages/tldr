# pbmtoascii

> Convert a PBM image to ASCII graphics.
> More information: <https://netpbm.sourceforge.net/doc/pbmtoascii.html>.

- Read PBM file as input and produce an ASCII output:

`pbmtoascii {{path/to/input_file}}`

- Read PBM file as input and save an ASCII output into a file:

`pbmtoascii {{path/to/input_file}} > {{path/to/output_file}}`

- Read PBM file as input setting the pixel mapping (defaults to 1x2):

`pbmtoascii -2x4 {{path/to/input_file}}`

- Display version information:

`pbmtoascii -version`
