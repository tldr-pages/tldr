# cmark

> Convertește textul formatat CommonMark Markdown în alte formate.
> Mai multe informaţii: <https://github.com/commonmark/cmark>

- Randați un fișier CommonMark Markdown la HTML:

`cmark --to html {{filename.md}}`

- Conversia datelor de la intrare standard la LaTeX:

`cmark --to latex`

- Conversia ghilimele drepte la ghilimele

`cmark --smart --to html {{filename.md}}`

- Validarea caracterelor UTF-8:

`cmark --validate-utf8 {{filename.md}}`
