# gitea

> Amministra Gitea, un leggero server di hosting Git.
> Richiede un file `app.ini` configurato o variabili d'ambiente.
> Maggiori informazioni: <https://docs.gitea.com/administration/command-line>.

- Avvia il server web Gitea usando la configurazione predefinita:

`gitea web`

- Crea lo schema e le tabelle necessarie del database:

`gitea migrate`

- Esegui sottocomandi amministrativi per la gestione degli utenti o dell’autenticazione:

`gitea admin {{user list}}`

- Mostra l’aiuto per un sottocomando specifico:

`gitea {{admin}} --help`

- Mostra l’aiuto:

`gitea help`

- Mostra la versione:

`gitea --version`
