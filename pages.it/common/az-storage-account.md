# az storage account

> Gestisce gli account di archiviazione in Azure.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/storage/account>.

- Crea un account di archiviazione:

`az storage account create {{[-n|--name]}} {{nome_account_archiviazione}} {{[-g|--resource-group]}} {{gruppo_risorse_azure}} --location {{posizione_azure}} --sku {{sku_account_archiviazione}}`

- Genera una firma di accesso condiviso per un account di archiviazione specifico:

`az storage account generate-sas --account-name {{nome_account_archiviazione}} {{[-n|--name]}} {{nome_account}} --permissions {{permessi_sas}} --expiry {{data_scadenza}} --services {{servizi_archiviazione}} --resource-types {{tipi_risorse}}`

- Elenca gli account di archiviazione:

`az storage account list {{[-g|--resource-group]}} {{gruppo_risorse_azure}}`

- Elimina un account di archiviazione specifico:

`az storage account delete {{[-n|--name]}} {{nome_account_archiviazione}} {{[-g|--resource-group]}} {{gruppo_risorse_azure}}`
