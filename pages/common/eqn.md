# eqn

> Equation preprocessor for the groff (GNU Troff) document formatting system.
> See also `troff` and `groff`.
> More information: <https://manned.org/eqn>.

- Process input with equations, saving the output for future typesetting with groff to PostScript:

`eqn {{filename.eqn}} > {{filename.roff}}`

- Typeset input with equations to [PDF] using the [me] macro package, saving the output:

`eqn -T {{pdf}} {{filename.eqn}} | groff -{{me}} -T {{pdf}} > {{filename.pdf}}`
