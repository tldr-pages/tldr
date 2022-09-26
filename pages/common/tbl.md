# tbl

> Table preprocessor for the groff (GNU Troff) document formatting system.
> See also `groff` and `troff`.
> More information: <https://manned.org/tbl>.

- Process input with tables, saving the output for future typesetting with groff to PostScript:

`tbl {{path/to/input_file}} > {{path/to/output.roff}}`

- Typeset input with tables to PDF using the [me] macro package:

`tbl -T {{pdf}} {{path/to/input.tbl}} | groff -{{me}} -T {{pdf}} > {{path/to/output.pdf}}`
