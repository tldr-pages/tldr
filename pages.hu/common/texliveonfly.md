# texliveonfly

> Letölti a hiányzó TeX Live csomagokat a `.tex` fájlok fordítása közben. További információ: <https://ctan.org/pkg/texliveonfly>.

- Hiányzó csomagok letöltése fordítás közben:

`texliveonfly {{source.tex}}`

- Egy adott fordító használata (alapértelmezett: `pdflatex`):

`texliveonfly --compiler={{compiler}} {{source.tex}}`

- Egyedi TeX Live `bin` mappa használata:

`texliveonfly --texlive_bin={{path/to/texlive_bin}} {{source.tex}}`
