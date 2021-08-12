# pdflatex

> Compilarea unui document PDF din fişierele sursă LaTeX.
> Mai multe informaţii: <https://manned.org/pdflatex>

- Compilarea unui document PDF:

`pdflatex {{source.tex}}`

- Compilarea unui document PDF care specifică un director de ieșire:

`pdflatex -output-directory={{path/to/directory}} {{source.tex}}`

- Compilați un document PDF, oprirea fiecărei erori:

`pdflatex -halt-on-error {{source.tex}}`
