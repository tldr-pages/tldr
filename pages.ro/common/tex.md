# tex

> Compilarea unui document DVI din fişierele sursă teX.
> Mai multe informaţii: <https://www.tug.org/begin.html>

- Compilarea unui document DVI:

`tex {{source.tex}}`

- Compilați un document DVI, specificând un director de ieșire:

`tex -output-directory={{path/to/directory}} {{source.tex}}`

- Compilați un document DVI, oprirea fiecărei erori:

`tex -halt-on-error {{source.tex}}`
