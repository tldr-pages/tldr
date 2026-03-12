# az storage container

> Gestisce i container di archiviazione blob in Azure.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/storage/container>.

- Crea un container in un account di archiviazione:

`az storage container create --account-name {{nome_account_archiviazione}} {{[-n|--name]}} {{nome_container}} --public-access {{livello_accesso}} --fail-on-exist`

- Genera una firma di accesso condiviso per il container:

`az storage container generate-sas --account-name {{nome_account_archiviazione}} {{[-n|--name]}} {{nome_container}} --permissions {{permessi_sas}} --expiry {{data_scadenza}} --https-only`

- Elenca i container in un account di archiviazione:

`az storage container list --account-name {{nome_account_archiviazione}} --prefix {{prefisso_filtro}}`

- Segna il container specificato per l'eliminazione:

`az storage container delete --account-name {{nome_account_archiviazione}} {{[-n|--name]}} {{nome_container}} --fail-not-exist`
