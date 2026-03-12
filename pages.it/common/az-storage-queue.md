# az storage queue

> Gestisce le code di archiviazione in Azure.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/storage/queue>.

- Crea una coda:

`az storage queue create --account-name {{nome_account_archiviazione}} {{[-n|--name]}} {{nome_coda}} --metadata {{metadati_coda}}`

- Genera una firma di accesso condiviso per la coda:

`az storage queue generate-sas --account-name {{nome_account_archiviazione}} {{[-n|--name]}} {{nome_coda}} --permissions {{permessi_coda}} --expiry {{data_scadenza}} --https-only`

- Elenca le code in un account di archiviazione:

`az storage queue list --prefix {{prefisso_filtro}} --account-name {{nome_account_archiviazione}}`

- Elimina la coda specificata e tutti i messaggi che contiene:

`az storage queue delete --account-name {{nome_account_archiviazione}} {{[-n|--name]}} {{nome_coda}} --fail-not-exist`
