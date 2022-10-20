# bup

> Sistema di backup basato sul formato dei packfile Git, fornendo salvataggi incrementali veloci e deduplicazione globale.
> Maggiori informazioni: <https://github.com/bup/bup>.

- Inizializza una repository di backup nella directory locale specificata:

`bup -d {{percorso/del/repository}} init`

- Prepara una certa directory prima di fare un backup:

`bup -d {{percorso/del/repository}} index {{percorso/della/directory}}`

- Esegui il backup di una directory in una repository locale:

`bup -d {{percorso/del/repository}} save -n {{nome_backup}} {{percorso/della/directory}}`

- Elenca i di backup attualmente nella repository:

`bup -d {{percorso/del/repository}} ls`

- Ripristina uno specifico backup in una determinata directory locale:

`bup -d {{percorso/del/repository}} restore -C {{percorso/della/destinazione}} {{nome_backup}}`
