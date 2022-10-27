# batch

> Esegui comandi nel futuro quando il carico di lavoro del sistema lo permette.
> Il servizio atd (o atrun) deve essere attivo per eseguire i comandi.
> Maggiori informazioni: <https://manned.org/batch>.

- Esegui i comandi inseriti standard input (premere `Ctrl + D` dopo aver inserito i comandi):

`batch`

- Esegui un comando da standard input:

`echo "{{./mio_script.sh}}" | batch`

- Esegui comandi contenuti in un dato file:

`batch -f {{percorso/del/file}}`
