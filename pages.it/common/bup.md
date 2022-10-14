# bup

> Sistema di backup basato sul formato dei packfile Git, fornendo salvataggi incrementali veloci e deduplicazione globale.
> Maggiori informazioni: <https://github.com/bup/bup>.

- Inizializza una repository di backup nella cartella locale specificata:

`bup -d {{percorso/a/repository}} init`

- Prepara una certa cartella prima di fare un backup:

`bup -d {{percorso/a/repository}} index {{percorso/a/cartella}}`

- Esegui il backup di una cartella in una repository locale:

`bup -d {{percorso/a/repository}} save -n {{nome_backup}} {{percorso/a/cartella}}`

- Elenca i di backup attualmente nella repository:

`bup -d {{percorso/a/repository}} ls`

- Ripristina uno specifico backup in una determinata cartella locale:

`bup -d {{percorso/a/repository}} restore -C {{percorso/a/destinazione}} {{nome_backup}}`
