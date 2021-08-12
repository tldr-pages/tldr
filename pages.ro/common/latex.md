# latex

> Compilarea unui document DVI din fișierele sursă LaTeX.
> Mai multe informaţii: <https://www.latex-project.org>

- Compilarea unui document DVI:

`latex {{source.tex}}`

- Compilați un document DVI, specificând un director de ieșire:

`latex -output-directory={{path/to/directory}} {{source.tex}}`

- Compilați un document DVI, oprirea fiecărei erori:

`latex -halt-on-error {{source.tex}}`
