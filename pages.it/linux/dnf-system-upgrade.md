# dnf system-upgrade

> Aggiorna Fedora a una nuova versione maggiore.
> Maggiori informazioni: <https://dnf5.readthedocs.io/en/latest/commands/system-upgrade.8.html>.

- Prepara il sistema aggiornando tutti i pacchetti installati:

`sudo dnf upgrade --refresh`

- Scarica i pacchetti richiesti per la nuova versione di release:

`sudo dnf system-upgrade download --releasever {{release_version}}`

- Riavvia e avvia il processo di aggiornamento:

`sudo dnf system-upgrade reboot`

- Mostra lo stato della transazione di aggiornamento corrente:

`sudo dnf system-upgrade status`

- Mostra i log dei tentativi di aggiornamento precedenti:

`sudo dnf system-upgrade log`

- Rimuove i dati e i pacchetti di aggiornamento in cache:

`sudo dnf system-upgrade clean`
