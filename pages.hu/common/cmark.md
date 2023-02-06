# cmark

> Átalakítja a CommonMark Markdown formátumú szöveget más formátumokra. További információ: <https://github.com/commonmark/cmark>.

- CommonMark Markdown fájl átalakítása HTML-be:

`cmark --to html {{filename.md}}`

- A szabványos bemenetről származó adatok konvertálása LaTeX-be:

`cmark --to latex`

- Egyenes idézőjelek átalakítása okos idézőjelekké:

`cmark --smart --to html {{filename.md}}`

- UTF-8 karakterek hitelesítése:

`cmark --validate-utf8 {{filename.md}}`
