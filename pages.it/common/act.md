# act

> Esegui GitHub Actions localmente usando Docker.
> Maggiori informazioni: <https://manned.org/act>.

- Elenca i job disponibili:

`act {{[-l|--list]}}`

- Esegui l'evento predefinito:

`act`

- Esegui un evento specifico:

`act {{evento}}`

- Esegui un job specifico:

`act {{[-j|--job]}} {{id_job}}`

- Non eseguire realmente le azioni (esecuzione simulata):

`act {{[-n|--dryrun]}}`

- Mostra log dettagliati:

`act {{[-v|--verbose]}}`

- Esegui un workflow specifico con evento push:

`act push {{[-W|--workflows]}} {{percorso/workflow}}`
