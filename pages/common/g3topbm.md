# g3topbm

> Convert a Group 3 fax file into a PBM image.
> More information: <https://netpbm.sourceforge.net/doc/g3topbm.html>.

- Convert a G3 fax file to a PBM file (padded to the longest line, salvaging what it can from transmission errors):

`g3topbm {{path/to/input.g3}} > {{path/to/output.pbm}}`

- Fail instead of salvaging the image when the input deviates from the G3 MH format:

`g3topbm -stop_error {{path/to/input.g3}} > {{path/to/output.pbm}}`

- Interpret bits least-significant first, for fax modems with the opposite bit order:

`g3topbm -reversebits {{path/to/input.g3}} > {{path/to/output.pbm}}`

- Stretch the image vertically by duplicating each row, for low-quality transmission mode:

`g3topbm -stretch {{path/to/input.g3}} > {{path/to/output.pbm}}`

- Assume a specific paper width instead of deriving it from the longest input line:

`g3topbm -paper_size={{A4}} {{path/to/input.g3}} > {{path/to/output.pbm}}`
