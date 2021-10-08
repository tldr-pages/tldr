# tbl

> Table preprocessor for the groff (GNU Troff) document formatting system.
> Input consists of plain text, troff formatting commands, and table formatting commands.
> See also `groff` and `troff`.
> More information: <https://manned.org/tbl>.

- Sample input table showing the four basic types of column.
  Note that the input contains hard tab characters between columns, not spaces,
  and that the contents on different rows do not always line up:

```troff
.TS
l c r n.
left-aligned	centered	right-aligned	numeric
text	text	text	123.45
.TE
```

- Sample input table showing an alternate column delimiter ([@] instead of tab),
  a header that spans multiple columns, special formatting for header rows and
  columns, and drawing lines between headers and the main table data:

```troff
.TS
tab({{@}});
cb s s s
lb | cb | rb | nb
=    =    =    =
lb | c    r    n.
Centered Bold Title Spans 4 Columns
Left Bold@Centered Bold@Right Bold@Numeric Bold
Bold header@centered text@right text@123.45
More bold@more centered@more right text@67.890
.TE
```

- Process input containing a table, saving the output as an intermediate file
  for future typesetting with groff to PostScript:

`tbl {{input_file}} > {{output_file.roff}}`

- Process input containing a table and typeset the result to [PDF] with groff
  using the [me] macro package, saving the output to a file:

```troff
tbl -T {{pdf}} {{input_file}} | groff -{{me}} -T {{pdf}} > {{outputfile.pdf}}
# OR
groff -t -T {{pdf}} -{{me}} {{input_file}} > {{outputfile.pdf}}
```
