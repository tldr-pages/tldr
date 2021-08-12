# pdftex

> Compilarea unui document PDF din fişierele sursă teX.
> Mai multe informaţii: <https://www.tug.org/applications/pdftex/>

- Compilarea unui document PDF:

`pdftex {{source.tex}}`

- Compilați un document PDF, specificând un director de ieșire:

`pdftex -output-directory={{path/to/directory}} {{source.tex}}`

- Compilați un document PDF, oprirea fiecărei erori:

`pdftex -halt-on-error {{source.tex}}`
