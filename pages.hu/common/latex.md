# latex

> DVI dokumentum összeállítása LaTeX forrásfájlokból. További információ: <https://www.latex-project.org>.

- DVI-dokumentum összeállítása:

`latex {{source.tex}}`

- DVI-dokumentum fordítása egy kimeneti könyvtár megadásával:

`latex -output-directory={{path/to/directory}} {{source.tex}}`

- DVI-dokumentum fordítása, minden hiba esetén kilépve:

`latex -halt-on-error {{source.tex}}`
