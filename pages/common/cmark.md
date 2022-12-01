# cmark

> Converts CommonMark Markdown formatted text to other formats.
> More information: <https://github.com/commonmark/cmark>.

- Render a CommonMark Markdown file to HTML:

`cmark --to html {{path/to/file.md}}`

- Convert data from standard input to LaTeX:

`cmark --to latex`

- Convert straight quotes to smart quotes:

`cmark --smart --to html {{path/to/file.md}}`

- Validate UTF-8 characters:

`cmark --validate-utf8 {{path/to/file.md}}`
