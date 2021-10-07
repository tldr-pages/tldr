# troff

> Typesetting processor for the groff (GNU Troff) document fomatting system.
> Input can be plain text, text with embedded formatting commands, or text
> with predefined formatting macros. Output must be converted to its final form
> by a device-dependent post-processor.
> More information: <https://manned.org/troff>

- Trivial example input with no formatting:

```
This is some simple input with line breaks after each sentence.
These few lines will be joined as necessary to wrap nicely.

A blank line is treated as a paragraph break.
```

- Example input with a few basic formatting commands:

```
.ce {{1}}       \" center the next 1 line
This line is centered
.sp {{0.5}}     \" skip {{0.5 lines}} of vertical space
.ti {{2}}       \" temporary indent {{2 ems}} -- "temporary" means 1 line only
This is the beginning of regular text. This "paragraph" has a little whitespace
before it and the first line is indented. This uses raw troff commands.
.sp {{0.5}}     \" skip {{0.5 lines}} of vertical space
.ti {{2}}       \" temporary indent {{2 ems}} -- "temporary" means 1 line only
This is a second "paragraph".
```

- Example input using the [me] macro package:

```
.ce {{1}}       \" raw troff commands still work
This line is centered
.pp
This is the beginning of regular text. This paragraph has a little whitespace
before it and the first line is indented. The size of both the vertical space
and the indent are controlled by troff variables.
.pp
This is a second paragraph.
```

- Format output for a PostScript printer, saving the output to a file:

```
troff {{input_file}} | grops > {{output_file.ps}}
```


- Format output for a PostScript printer using the [me] macro package,
  saving the output to a file:

```
troff -{{me}} {{input_file}} | grops > {{output_file.ps}}
```

- Format output as [a]SCII text using the [man] macro package:

```
troff -T {{ascii}} -{{man}} {{input_file}} | grotty
```

- Format output as a [pdf] file, saving the output to a file:

`troff -T {{pdf}} {{input_file}} | gropdf > {{output_file.pdf}}`

