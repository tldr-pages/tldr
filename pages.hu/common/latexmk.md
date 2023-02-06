# latexmk

> A LaTeX forrásfájlokat kész dokumentumokká fordítja. Szükség esetén automatikusan többszörös futtatást végez. További információ: <https://mg.readthedocs.io/latexmk.html>.

- DVI (eszközfüggetlen fájl) dokumentum összeállítása minden forrásból:

`latexmk`

- DVI-dokumentum összeállítása egy adott forrásfájlból:

`latexmk {{source.tex}}`

- PDF dokumentum összeállítása:

`latexmk -pdf {{source.tex}}`

- A dokumentum generálásának kikényszerítése hibák esetén is:

`latexmk -f {{source.tex}}`

- Egy adott TEX-fájlhoz létrehozott ideiglenes TEX-fájlok megtisztítása:

`latexmk -c {{source.tex}}`

- Az aktuális könyvtárban lévő összes ideiglenes TEX-fájl kitakarítása:

`latexmk -c`
