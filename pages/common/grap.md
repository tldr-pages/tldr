# grap

> A charting preprocessor for the groff (GNU Troff) document formatting system.
> See also `pic` and `groff`.
> More information: <https://manned.org/grap>.

- Process a `grap` file and save the output file for future processing with `pic` and `groff`:

`grap {{path/to/input.grap}} > {{path/to/output.pic}}`

- Typeset a `grap` file to PDF using the [me] macro package, saving the output to a file:

`grap {{path/to/input.grap}} | pic -T {{pdf}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}`
