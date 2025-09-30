# latex

> Compileer een DVI-document van LaTeX bronbestanden.
> Meer informatie: <https://www.latex-project.org>.

- Compileer een DVI-document:

`latex {{bron.tex}}`

- Compileer een DVI-document naar een specifieke output map:

`latex -output-directory={{pad/naar/map}} {{bron.tex}}`

- Compileer een DVI-document en sluit af als er een fout optreedt:

`latex -halt-on-error {{bron.tex}}`
