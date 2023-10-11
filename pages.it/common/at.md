# at

> Programma l'esecuzione di comandi nel futuro.
> Il servizio atd (o atrun) deve essere attivo per eseguire i comandi.
> Maggiori informazioni: <https://manned.org/at>.

- Esegui i comandi inseriti standard input tra 5 minuti (premere `Ctrl + D` dopo aver inserito i comandi):

`at now + 5 minutes`

- Esegui un comando passato da standard input alle 10:00 di mattina:

`echo "{{./mio_script.sh}}" | at 1000`

- Esegui comandi contenuti in un dato file il prossimo martedì alle 9:30 di sera:

`at -f {{percorso/del/file}} 9:30 PM Tue`
