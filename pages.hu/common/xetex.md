# xetex

> PDF dokumentum összeállítása XeTeX forrásfájlokból. További információ: <https://www.tug.org/xetex/>.

- PDF dokumentum összeállítása:

`xetex {{source.tex}}`

- PDF-dokumentum összeállítása egy kimeneti könyvtár megadásával:

`xetex -output-directory={{path/to/directory}} {{source.tex}}`

- PDF-dokumentum fordítása, hiba esetén kilépés:

`xetex -halt-on-error {{source.tex}}`
