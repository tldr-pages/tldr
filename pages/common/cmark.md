# cmark

> Convert CommonMark Markdown formatted text to other formats.
> More information: <https://github.com/commonmark/cmark>.

- Render a CommonMark Markdown file to HTML:

`cmark --to html {{filename.md}}`

- Convert data from `stdin` to LaTeX:

`cmark --to latex`

- Convert straight quotes to smart quotes:

`cmark --smart --to html {{filename.md}}`

- Validate UTF-8 characters:

`cmark --validate-utf8 {{filename.md}}`
