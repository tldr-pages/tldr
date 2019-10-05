# du

> Utilizzo del disco: stima e riassumi lo spazio utilizzato da file e directory.

- Elenca le dimensioni di una directory ed ogni sotto-directory, nell'unità specificata (B/KB/MB):

`du -{{b|k|m}} {{percorso/alla/directory}}`

- Elenca le dimensioni di una directory ed ogni sotto-directory, in formato umanamente leggibile (seleziona automaticamente l'unità appropriata per ogni dimensione):

`du -h {{percorso/alla/directory}}`

- Mostra la dimensione di una singola directory, in unità umanamente leggibili:

`du -sh {{percorso/alla/directory}}`

- Mostra in formato umanamente leggibile le dimensioni di una directory e tutti i file e directory in essa contenuti:

`du -ah {{percorso/alla/directory}}`

- Elenca le dimensioni umanamente leggibili di una directory e d ogni sotto-directory, fino ad N livelli di profondità:

`du -h --max-depth=N {{percorso/alla/directory}}`

- Mostra le dimensioni umanamente leggibili di tutti i file .jpg nelle sottocartelle della cartella corrente, e mostra il totale cumulativo alla fine:

`du -ch */*.jpg`
