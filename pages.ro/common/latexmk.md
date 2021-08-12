# latexmk

> Compilați fișierele sursă LaTeX în documente finite.
> Efectuează automat mai multe rulări atunci când este necesar.
> Mai multe informaţii: <https://mg.readthedocs.io/latexmk.html>

- Compilarea unui document DVI (Device Independent file) din fiecare sursă:

`latexmk`

- Compilarea unui document DVI dintr-un fișier sursă specific:

`latexmk {{source.tex}}`

- Compilarea unui document pdf:

`latexmk -pdf {{source.tex}}`

- Forțați generarea unui document, chiar dacă există erori:

`latexmk -f {{source.tex}}`

- Curățați fișierele tex temporare create pentru un anumit fișier tex:

`latexmk -c {{source.tex}}`

- Curățați toate fișierele tex temporare din directorul curent:

`latexmk -c`
