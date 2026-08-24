# csvcut

> Filtra e tronca file CSV. Come il comando Unix `cut`, ma per dati tabellari.
> Incluso in csvkit.
> Maggiori informazioni: <https://csvkit.readthedocs.io/en/latest/scripts/csvcut.html>.

- Stampa indici e nomi di tutte le colonne:

`csvcut {{[-n|--names]}} {{dati.csv}}`

- Estrai la prima e terza colonna:

`csvcut {{[-c|--columns]}} {{1,3}} {{dati.csv}}`

- Estrai tutte le colonne eccetto la quarta:

`csvcut {{[-C|--not-columns]}} {{4}} {{dati.csv}}`

- Estrai le colonne "id" e "nome di battesimo" (in quest'ordine):

`csvcut {{[-c|--columns]}} {{id,"nome di battesimo"}} {{dati.csv}}`
