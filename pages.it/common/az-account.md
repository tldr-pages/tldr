# az account

> Gestisce le informazioni di sottoscrizione Azure.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/account>.

- Elenca tutte le sottoscrizioni per l'account loggato:

`az account list`

- Imposta una `sottoscrizione` come quella attualmente attiva:

`az account set {{[-s|--subscription]}} {{id_sottoscrizione}}`

- Elenca le regioni supportate per la sottoscrizione attualmente attiva:

`az account list-locations`

- Stampa un token di accesso da usare con `MS Graph API`:

`az account get-access-token --resource-type {{ms-graph}}`

- Stampa i dettagli della sottoscrizione attualmente attiva in un formato specifico:

`az account show {{[-o|--output]}} {{json|tsv|table|yaml}}`
