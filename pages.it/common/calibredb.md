# calibredb

> Strumentoi per gestire il tuo database di eBook.
> Parte del manager di eBook Calibre.
> Maggiori informazioni: <https://manual.calibre-ebook.com/generated/en/calibredb.html>.

- Elenca gli eBook nella libreria con informazioni aggiuntive:

`calibredb list`

- Cerca tra gli eBook mostrando informazioni aggiuntive:

`calibredb list --search {{termine_di_ricerca}}`

- Cerca mostrando solamente gli ID degli eBook:

`calibredb search {{termine_di_ricerca}}`

- Aggiungi uno o più eBook alla libreria:

`calibredb add {{file1 file2 …}}`

- Rimuovi uno o più eBook dalla libreria. Sono necessari gli ID (vedi sopra):

`calibredb remove {{id1 id2 …}}`
