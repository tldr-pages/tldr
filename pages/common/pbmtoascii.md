# pbmtoascii

> Convert a PBM image to ASCII graphics.
> See also: `ppmtoascii`, `asciitopgm`, `ppmtoterm`.
> More information: <https://netpbm.sourceforge.net/doc/pbmtoascii.html>.

- Read a PBM file as input and produce an ASCII output:

`pbmtoascii {{path/to/input_file.pbm}}`

- Read a PBM file as input and save an ASCII output into a file:

`pbmtoascii {{path/to/input_file.pbm}} > {{path/to/output_file}}`

- Read a PBM file as input while setting the pixel mapping (defaults to 1x2):

`pbmtoascii -{{1x2|2x4}} {{path/to/input_file.pbm}}`

- Display version:

`pbmtoascii -version`
