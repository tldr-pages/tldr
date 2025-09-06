# pbmmake

> Create a blank bitmap.
> More information: <https://netpbm.sourceforge.net/doc/pbmmake.html>.

- Create a blank bitmap of the specified dimensions:

`pbmmake {{width}} {{height}} > {{path/to/output_file.pbm}}`

- Specify the color of the created bitmap:

`pbmmake -{{white|black|grey}} {{width}} {{height}} > {{path/to/output_file.pbm}}`
