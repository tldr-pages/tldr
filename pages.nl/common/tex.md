# tex

> Compileer een DVI-document van TeX bronbestanden.
> Meer informatie: <https://www.tug.org/begin.html>.

- Compileer een DVI-document:

`tex {{bron.tex}}`

- Compileer een DVI-document naar een specifieke output map:

`tex -output-directory={{pad/naar/map}} {{bron.tex}}`

- Compileer een DVI-document en sluit af als er een fout optreedt:

`tex -halt-on-error {{bron.tex}}`
