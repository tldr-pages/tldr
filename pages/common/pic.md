# pic

> Picture preprocessor for the groff (GNU Troff) document formatting system.
> Input consists of plain text, troff formatting commands, troff macros, and picture formatting commands.
> See also `groff` and `troff`.
> More information: <https://manned.org/pic>.

- Sample input picture of a rectangle containing a label:

```troff
.PS
  box "a label"
.PE
```

- Sample input that draws three ellipses resembling a head with two ears:
  
```troff
.PS
  ellipse
  ellipse ht .2 wid .3 with .se at 1st ellipse.nw
  ellipse ht .2 wid .3 with .sw at 1st ellipse.ne
.PE
```

- Process input containing a picture, saving the output as an intermediate file
  for future typesetting with groff to PostScript:

`pic {{input_file}} > {{output_file.roff}}`

- Process input containing a picture and typeset the result to [PDF] with groff
  using the [me] macro package, saving the output to a file:

```bash
pic -T {{pdf}} {{input_file}} | groff -{{me}} -T {{pdf}} > {{outputfile.pdf}}
# OR
groff -p -T {{pdf}} -{{me}} {{input_file}} > {{outputfile.pdf}}
```
