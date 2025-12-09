# ftp

> Trasferisci file in modo interattivo tra un server FTP locale e remoto.
> Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/ftp>.

- Connettiti a un server FTP remoto:

`ftp {{host}}`

- Accedi come utente anonimo:

`ftp -A {{host}}`

- Disabilita l'accesso automatico alla connessione iniziale:

`ftp -n {{host}}`

- Esegui un file contenente una lista di comandi FTP:

`ftp -s:{{percorso\to\file}} {{host}}`

- Carica file (espressione glob):

`mget {{*.png}}`

- Carica file (espressione glob):

`mput {{*.zip}}`

- Cancella file sul server remoto:

`mdelete {{*.txt}}`

- Mostra la pagina di aiuto dettagliato:

`ftp --help`
