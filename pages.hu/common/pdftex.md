# pdftex

> PDF dokumentum összeállítása TeX forrásfájlokból. További információ: <https://www.tug.org/applications/pdftex/>.

- PDF dokumentum összeállítása:

`pdftex {{source.tex}}`

- PDF-dokumentum összeállítása a kimeneti könyvtár megadásával:

`pdftex -output-directory={{path/to/directory}} {{source.tex}}`

- PDF-dokumentum fordítása, minden hiba esetén kilépve:

`pdftex -halt-on-error {{source.tex}}`
