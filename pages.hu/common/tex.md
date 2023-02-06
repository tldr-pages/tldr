# tex

> DVI dokumentum összeállítása TeX forrásfájlokból. További információ: <https://www.tug.org/begin.html>.

- DVI dokumentum összeállítása:

`tex {{source.tex}}`

- DVI-dokumentum fordítása egy kimeneti könyvtár megadásával:

`tex -output-directory={{path/to/directory}} {{source.tex}}`

- DVI-dokumentum fordítása, minden hiba esetén kilépve:

`tex -halt-on-error {{source.tex}}`
