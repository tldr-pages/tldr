# grap

> A charting preprocessor for the groff (GNU Troff) document formatting system.
> Input consists of plain text, troff formatting commands, troff macros, and special graph formatting commands.
> Technically grap converts descriptions of graphs into pictures, which then get rendered using pic and groff/troff.
> See also `pic` and `groff`.
> More information: <https://manned.org/grap>.

- Sample input for generating a scatter plot of 5 points:

```troff
.G1
1 1
2 4
3 9
4 16
5 25
.G2
```

- Sample input for generating a scatter plot of points from an external data
  file named [data.tsv]:

```troff
.G1
copy "{{data.tsv}}"
.G2
```

- Sample input for generating a simple bar chart:

```troff
.G1
bar up 1 ht 1   wid 0.5
bar up 2 ht 4   wid 0.5
bar up 3 ht 9   wid 0.5
bar up 4 ht 16  wid 0.5
bar up 5 ht 25  wid 0.5
.G2
```

- Sample input for plotting bars where the bottoms rise above the X axis:

```troff
.G1
bar up 1 ht 1   wid 0.5 base 1
bar up 2 ht 4   wid 0.5 base 2
bar up 3 ht 9   wid 0.5 base 3
bar up 4 ht 16  wid 0.5 base 4
bar up 5 ht 25  wid 0.5 base 5
.G2
```

- Process input containing a graph, saving the output as an intermediate file
  for future processing with pic and groff to PostScript:

`grap {{input_file}} > {{output_file.pic}}`

- Process input containing a graph and typeset the result to [PDF] with pic
  and groff using the [me] macro package, saving the output to a file:

```bash
grap {{input_file}} | pic -T {{pdf}} | groff -{{me}} -T {{pdf}} > {{outputfile.pdf}}
# OR
groff -G -p -T {{pdf}} -{{me}} {{output_file}} > {{outputfile.pdf}}
```
