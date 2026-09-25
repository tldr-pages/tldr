# brew services

> Gestisci i servizi in background con `launchctl` su macOS o `systemctl` su Linux.
> Maggiori informazioni: <https://docs.brew.sh/Manpage#services-subcommand>.

- Elenca tutti i servizi gestiti per l'utente corrente:

`brew services`

- Elenca ulteriori informazioni su tutti i servizi gestiti:

`brew services info --all`

- Avvia immediatamente un servizio e registralo per l'avvio al login (o all'avvio):

`brew services start {{formula}}`

- Ferma immediatamente il servizio e rimuovilo dall'avvio al login (o all'avvio):

`brew services stop {{formula}}`

- Ferma (se necessario) e avvia immediatamente il servizio, quindi registralo per l'avvio al login (o all'avvio):

`brew services restart {{formula}}`

- Rimuovi tutti i servizi non più usati:

`brew services cleanup`
