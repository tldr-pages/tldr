# calibredb

> Strumentoi per gestire il tuo database di e-book.
> Parte del manager di e-book Calibre.
> Maggiori informazioni: <https://manual.calibre-ebook.com/generated/en/calibredb.html>.

- Elenca gli e-book nella libreria con informazioni aggiuntive:

`calibredb list`

- Cerca tra gli e-book mostrando informazioni aggiuntive:

`calibredb list --search {{termine_di_ricerca}}`

- Cerca mostrando solamente gli ID degli e-book:

`calibredb search {{termine_di_ricerca}}`

- Aggiungi uno o più e-book alla libreria:

`calibredb add {{percoso/del/file1 percoso/del/file2 ...}}`

- Aggiungere ricorsivamente tutti gli e-book in una directory alla libreria:

`calibredb add {{[-r|--recurse]}} {{percoso/della/directory}}`

- Rimuovi uno o più e-book dalla libreria. Sono necessari gli ID (vedi sopra):

`calibredb remove {{id1 id2 ...}}`
