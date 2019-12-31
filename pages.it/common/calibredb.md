# calibredb

> Strumentoi per gestire il tuo database di ebook.
> Parte del manager di ebook Calibre.
> Maggiori informazioni: <https://manual.calibre-ebook.com/generated/en/calibredb.html>.

- Elenca gli ebook nella libreria con informazioni aggiuntive:

`calibredb list`

- Cerca tra gli ebook mostrando informazioni aggiuntive:

`calibredb list --search {{termine_di_ricerca}}`

- Cerca mostrando solamente gli ID degli ebook:

`calibredb search {{termine_di_ricerca}}`

- Aggiungi uno o più ebook alla libreria:

`calibredb add {{file1 file2 …}}`

- Rimuovi uno o più ebook dalla libreria. Sono necessari gli ID (vedi sopra):

`calibredb remove {{id1 id2 …}}`
