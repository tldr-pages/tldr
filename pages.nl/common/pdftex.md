# pdftex

> Compileer een PDF-document van TeX bronbestanden.
> Meer informatie: <https://www.tug.org/applications/pdftex/>.

- Compileer een PDF-document:

`pdftex {{bron.tex}}`

- Compileer een PDF-document naar een specifieke output map:

`pdftex -output-directory={{pad/naar/map}} {{bron.tex}}`

- Compileer een PDF-document en sluit af als er een fout optreedt:

`pdftex -halt-on-error {{bron.tex}}`
