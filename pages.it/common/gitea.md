# gitea

Uno strumento da riga di comando per amministrare Gitea, un server Git leggero e autogestito.

> Richiede un file `app.ini` configurato o variabili d'ambiente.
> Maggiori informazioni: <https://docs.gitea.com/administration/command-line>.

- Mostra i comandi disponibili:
  ```sh
  gitea help
    ````

* Avvia il server web Gitea usando la configurazione predefinita:

  ```sh
  gitea web
  ```

* Mostra la versione attuale di Gitea:

  ```sh
  gitea --version
  ```

* Crea lo schema e le tabelle nel database:

  ```sh
  gitea migrate
  ```

* Esegui comandi amministrativi integrati (come la gestione utenti):

  ```sh
  gitea admin user list
  ```

* Mostra la guida di un sottocomando specifico:

  ```sh
  gitea admin --help
  ```
