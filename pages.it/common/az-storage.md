# az storage

> Gestisce le risorse di Archiviazione cloud di Azure.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/storage>.

- Crea un account di archiviazione specificando una posizione:

`az storage account create {{[-g|--resource-group]}} {{nome_gruppo}} {{[-n|--name]}} {{nome_account}} {{[-l|--location]}} {{posizione}} --sku {{sku_account}}`

- Elenca tutti gli account di archiviazione in un gruppo di risorse:

`az storage account list {{[-g|--resource-group]}} {{nome_gruppo}}`

- Elenca le chiavi di accesso per un account di archiviazione:

`az storage account keys list {{[-g|--resource-group]}} {{nome_gruppo}} {{[-n|--name]}} {{nome_account}}`

- Elimina un account di archiviazione:

`az storage account delete {{[-g|--resource-group]}} {{nome_gruppo}} {{[-n|--name]}} {{nome_account}}`

- Aggiorna l'impostazione della versione minima TLS per un account di archiviazione:

`az storage account update --min-tls-version {{TLS1_0|TLS1_1|TLS1_2}} {{[-g|--resource-group]}} {{nome_gruppo}} {{[-n|--name]}} {{nome_account}}`
