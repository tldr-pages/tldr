# cmark

> Converte testo CommonMark Markdown in altri formati.
> Maggiori informazioni: <https://manned.org/cmark>.

- Converti un file Markdown in HTML:

`cmark --to html {{file.md}}`

- Converti in LaTeX da `stdin`:

`cmark --to latex`

- Converti apici semplici in apici intelligenti:

`cmark --smart --to html {{file.md}}`

- Converti validando i caratteri UTF-8:

`cmark --validate-utf8 {{file.md}}`
