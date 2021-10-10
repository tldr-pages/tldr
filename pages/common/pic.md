# pic

> Picture preprocessor for the groff (GNU Troff) document formatting system.
> See also `groff` and `troff`.
> More information: <https://manned.org/pic>.

- Process input with pictures, saving the output for future typesetting with groff to PostScript:

`pic {{filename.pic}} > {{filename.roff}}`

- Typeset input with pictures to [PDF] using the [me] macro package, saving the output:

`pic -T {{pdf}} {{filename.pic}} | groff -{{me}} -T {{pdf}} > {{filename.pdf}}`
