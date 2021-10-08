# groff

> Typesetting program that reads plain text mixed with formatting commands and produces formatted output.
> It is the GNU replacement for the `troff` and `nroff` Unix command for text formatting.
> More information: <https://www.gnu.org/software/groff>.

- Trivial example input with no formatting:

```
This is some simple input with line breaks after each sentence.
These few lines will be joined as necessary to wrap nicely.

A blank line is treated as a paragraph break.
```

- Example input with a few basic formatting commands:

```troff
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

```troff
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

`groff {{input_file}} > {{output_file.ps}}`

- Render a man page using the ASCII output device, and display it using a pager:

`groff -man -T ascii {{manpage.1}} | less`

- Render a man page into an HTML file:

`groff -man -T html {{manpage.1}} > {{page.html}}`

- Process a roff file using the `tbl` and `pic` preprocessors, and the `me`
  macro set, to PDF, saving the output to a file:

`groff -t -p -me -T pdf {{foo.me}} > {{foo.pdf}}`

- Run a `groff` command with preprocessor and macro options guessed by the `grog` utility:

`eval "$(grog -T utf8 {{foo.me}})"`
