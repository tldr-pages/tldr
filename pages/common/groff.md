# groff

> GNU replacement for the `troff` and `nroff` typesetting utilities.
> More information: <https://www.gnu.org/software/groff>.

- Format output for a PostScript printer, saving the output to a file:

`groff {{filename.roff}} > {{filename.ps}}`

- Render a man page using the ASCII output device, and display it using a pager:

`groff -man -T ascii {{manpage.1}} | less`

- Render a man page into an HTML file:

`groff -man -T html {{manpage.1}} > {{manpage.html}}`

- Process a roff file using the `tbl` and `pic` preprocessors, and the `me`
  macro set, to PDF, saving the output to a file:

`groff -t -p -me -T pdf {{foo.me}} > {{foo.pdf}}`

- Run a `groff` command with preprocessor and macro options guessed by the `grog` utility:

`eval "$(grog -T utf8 {{foo.me}})"`
