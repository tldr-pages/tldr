# cmark

> Converte testo CommonMark Markdown in altri formati.
> Maggiori informazioni: <https://github.com/commonmark/cmark>.

- Converti un file Markdown in HTML:

`cmark --to html {{file.md}}`

- Converti in latex da standard input:

`cmark --to latex`

- Converti apici semplici in apici intelligenti:

`cmark --smart --to html {{file.md}}`

- Converti validando i caratteri UTF8:

`cmark --validate-utf8 {{file.md}}`
