# gitea

> Uno strumento da riga di comando per amministrare Gitea, un server Git leggero e autogestito.
> Richiede un file `app.ini` configurato o variabili d'ambiente.
> Maggiori informazioni: <https://docs.gitea.com/administration/command-line>.

- Avvia il server web Gitea usando la configurazione predefinita:

`gitea web`

- Crea lo schema e le tabelle nel database:

`gitea migrate`

- Esegui comandi amministrativi integrati (come la gestione utenti):

`gitea admin user list`

- Mostra la guida di un sottocomando specifico:

`gitea admin --help`

- Mostra i comandi disponibili:

`gitea help`

- Mostra la versione attuale di Gitea:

`gitea --version`
