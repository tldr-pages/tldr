# pdflatex

> PDF dokumentum összeállítása LaTeX forrásfájlokból. További információ: <https://manned.org/pdflatex>.

- PDF dokumentum összeállítása:

`pdflatex {{source.tex}}`

- PDF-dokumentum összeállítása egy kimeneti könyvtár megadásával:

`pdflatex -output-directory={{path/to/directory}} {{source.tex}}`

- PDF-dokumentum fordítása, minden hiba esetén kilépve:

`pdflatex -halt-on-error {{source.tex}}`
