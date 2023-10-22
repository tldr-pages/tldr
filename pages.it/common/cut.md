# cut

> Taglia dividendo in campi `stdin` o file.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/cut>.

- Estrai i primi 16 caratteri di ogni riga da `stdin`:

`cut -c {{1-16}}`

- Estrai i primi 16 caratteri di ogni riga da un dato file:

`cut -c {{1-16}} {{file}}`

- Estrai tutto dal terzo carattere fino alla fine di ogni riga:

`cut -c {{3-}}`

- Estrai il quinto campo di ogni linea, utilizzando i due punti come separatore di campo (il default è tab):

`cut -d'{{:}}' -f{{5}}`

- Estrai il secondo e decimo campo di ogni linea, utilizzando il punto e virgola come delimitatore:

`cut -d'{{;}}' -f{{2,10}}`

- Estrai i campi dal terzo in poi di ogni linea, utilizzando lo spazio come delimitatore:

`cut -d'{{ }}' -f{{3-}}`
