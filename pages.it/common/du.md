# du

> Utilizzo del disco: stima e riassumi lo spazio utilizzato da file e directory.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/du>.

- Elenca le dimensioni di una directory ed ogni sotto-directory, nell'unità specificata (B/KiB/MiB):

`du -{{b|k|m}} {{percorso/della/directory}}`

- Elenca le dimensioni di una directory ed ogni sotto-directory, in formato umanamente leggibile (seleziona automaticamente l'unità appropriata per ogni dimensione):

`du -h {{percorso/della/directory}}`

- Mostra la dimensione di una singola directory, in unità umanamente leggibili:

`du -sh {{percorso/della/directory}}`

- Mostra in formato umanamente leggibile le dimensioni di una directory e tutti i file e directory in essa contenuti:

`du -ah {{percorso/della/directory}}`

- Elenca le dimensioni umanamente leggibili di una directory e d ogni sotto-directory, fino ad N livelli di profondità:

`du -h --max-depth=N {{percorso/della/directory}}`

- Mostra le dimensioni umanamente leggibili di tutti i file `.jpg` nelle sottodirectory della directory corrente, e mostra il totale cumulativo alla fine:

`du -ch {{*/*.jpg}}`
