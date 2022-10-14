# du

> Utilizzo del disco: stima e riassumi lo spazio utilizzato da file e cartelle.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/du>.

- Elenca le dimensioni di una cartella ed ogni sotto-cartella, nell'unità specificata (B/KiB/MiB):

`du -{{b|k|m}} {{percorso/della/cartella}}`

- Elenca le dimensioni di una cartella ed ogni sotto-cartella, in formato umanamente leggibile (seleziona automaticamente l'unità appropriata per ogni dimensione):

`du -h {{percorso/della/cartella}}`

- Mostra la dimensione di una singola cartella, in unità umanamente leggibili:

`du -sh {{percorso/della/cartella}}`

- Mostra in formato umanamente leggibile le dimensioni di una cartella e tutti i file e cartelle in essa contenuti:

`du -ah {{percorso/della/cartella}}`

- Elenca le dimensioni umanamente leggibili di una cartella e d ogni sotto-cartella, fino ad N livelli di profondità:

`du -h --max-depth=N {{percorso/della/cartella}}`

- Mostra le dimensioni umanamente leggibili di tutti i file `.jpg` nelle sottocartelle della cartella corrente, e mostra il totale cumulativo alla fine:

`du -ch */*.jpg`
