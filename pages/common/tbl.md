# tbl

> Table preprocessor for the groff (GNU Troff) document formatting system.
> See also `groff` and `troff`.
> More information: <https://manned.org/tbl>.

- Process input with tables, saving the output for future typesetting with groff to PostScript:

`tbl {{input_file}} > {{output_file.roff}}`

- Typeset input with tables to [PDF] using the [me] macro package, saving the output:

`tbl -T {{pdf}} {{filename.tbl}} | groff -{{me}} -T {{pdf}} > {{filename.pdf}}`
