# cmark

> Converts CommonMark Markdown formatted text to other formats.
> More information: <https://github.com/commonmark/cmark>.

- Render a Commonmark Markdown file to HTML:

`cmark --to html {{filename.md}}`

- Convert data from standard input to latex:

`cmark --to latex`

- Convert straight quotes to smart quotes:

`cmark --smart --to html {{filename.md}}`

- Validate utf8 characters:

`cmark --validate-utf8 {{filename.md}}`
