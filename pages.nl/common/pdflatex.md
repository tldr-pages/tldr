# pdflatex

> Compileer een PDF-document van LaTeX bronbestanden.
> Meer informatie: <https://manned.org/pdflatex>.

- Compileer een PDF-document:

`pdflatex {{bron.tex}}`

- Compileer een PDF-document naar een specifieke output map:

`pdflatex -output-directory={{pad/naar/map}} {{bron.tex}}`

- Compileer een PDF-document en sluit af als er een fout optreedt:

`pdflatex -halt-on-error {{bron.tex}}`
