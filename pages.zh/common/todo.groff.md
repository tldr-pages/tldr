# groff

> Typesetting program that reads plain text mixed with formatting commands and produces formatted output.
> It is the GNU replacement for the `troff` and `nroff` Unix commands for text formatting.
> More information: <https://www.gnu.org/software/groff>.

- Render a man page as plain text, and display the result:

`groff -man -T utf8 {{manpage.1}}`

- Render a man page using the ASCII output device, and display it using a pager:

`groff -man -T ascii {{manpage.1}} | less`

- Render a man page into an HTML file:

`groff -man -T html {{manpage.1}} > {{page.html}}`

- Process a roff file using the `tbl` and `pic` preprocessors, and the `me` macro set:

`groff -t -p -me -T utf8 {{foo.me}}`

- Run a `groff` command with preprocessor and macro options guessed by the `grog` utility:

`eval "$(grog -T utf8 {{foo.me}})"`
