# groff

> GNU replacement for the `troff` and `nroff` typesetting utilities.
> More information: <https://www.gnu.org/software/groff>.

- Format output for a PostScript printer, saving the output to a file:

`groff {{filename.roff}} > {{filename.ps}}`

- Render a man page using the ASCII output device, and display it using a pager:

`groff -man -T ascii {{manpage.1}} | less`

- Render a man page into an HTML file:

`groff -man -T html {{manpage.1}} > {{manpage.html}}`

- Typeset a roff file containing [t]ables and [p]ictures, using the [me] macro set, to PDF, saving the output:

`groff {{-t}} {{-p}} -{{me}} -T {{pdf}} {{filename.me}} > {{filename.pdf}}`

- Run a `groff` command with preprocessor and macro options guessed by the `grog` utility:

`eval "$(grog -T utf8 {{foo.me}})"`
