# troff

> Typesetting processor for the groff (GNU Troff) document fomatting system.
> See also `groff`.
> More information: <https://manned.org/troff>.

- Format output for a PostScript printer, saving the output to a file:

`troff {{filename.roff}} | grops > {{filename.ps}}`

- Format output for a PostScript printer using the [me] macro package, saving the output to a file:

`troff -{{me}} {{filename.roff}} | grops > {{filename.ps}}`

- Format output as [a]SCII text using the [man] macro package:

`troff -T {{ascii}} -{{man}} {{filename.roff}} | grotty`

- Format output as a [pdf] file, saving the output to a file:

`troff -T {{pdf}} {{filename.roff}} | gropdf > {{filename.pdf}}`
