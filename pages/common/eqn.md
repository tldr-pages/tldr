# eqn

> Equation preprocessor for the groff (GNU Troff) document formatting system.
> Input consists of plain text, troff formatting commands, troff macros, and special equation formatting commands.
> See also `troff` and `groff`.
> More information: <https://manned.org/eqn>.

- Sample input with both block and inline equations:

```troff
Newton's law of gravitation
.EQ
delim $$
F sub 12 = { G m sub 1 m sub 2 } over r sup 2
.EN
says that the force $F sub 12$ exerted by
a particle with mass $m sub 1$
on another particle with mass $m sub 2$
is proportional to the
.i square       \" me macro for italics
of the distance $r$ between them.
```

- Process input with equations, saving the output as an intermediate file
  for future typesetting with groff to PostScript:

`eqn {{input_file}} > {{output_file.roff}}`

- Process input with equations and typeset the result to [PDF] with groff
  using the [me] macro package, saving the output to a file:

```bash
eqn -T {{pdf}} {{input_file}} | groff -{{me}} -T {{pdf}} > {{output_file.pdf}}
# OR
groff -e -T {{pdf}} -{{me}} {{input_file}} > {{output_file.pdf}}
```
