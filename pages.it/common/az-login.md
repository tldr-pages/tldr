# az login

> Accedi ad Azure.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/reference-index#az-login>.

- Accedi in modo interattivo:

`az login`

- Accedi con un principal del servizio usando un segreto client:

`az login --service-principal {{[-u|--username]}} {{http://azure-cli-service-principal}} {{[-p|--password]}} {{segreto}} {{[-t|--tenant]}} {{someone.onmicrosoft.com}}`

- Accedi con un principal del servizio usando un certificato client:

`az login --service-principal {{[-u|--username]}} {{http://azure-cli-service-principal}} {{[-p|--password]}} {{percorso/verso/cert.pem}} {{[-t|--tenant]}} {{someone.onmicrosoft.com}}`

- Accedi usando l'identità assegnata dal sistema di una VM:

`az login {{[-i|--identity]}}`

- Accedi usando l'identità assegnata dall'utente di una VM:

`az login {{[-i|--identity]}} {{[-u|--username]}} /subscriptions/{{id_sottoscrizione}}/resourcegroups/{{mio_rg}}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{{mio_id}}`
