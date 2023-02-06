# az storage account

> Tárolási fiókok kezelése az Azure-ban. A `azure-cli` weboldal része. További információ: <https://learn.microsoft.com/cli/azure/storage/account>.

- Tárolási fiók létrehozása:

`az storage account create --name {{storage_account_name}} --resource-group {{azure_resource_group}} --location {{azure_location}} --sku {{storage_account_sku}}`

- Megosztott hozzáférési aláírás létrehozása egy adott tárolófiókhoz:

`az storage account generate-sas --account-name {{storage_account_name}} --name {{account_name}} --permissions {{sas_permissions}} --expiry {{expiry_date}} --services {{storage_services}} --resource-types {{resource_types}}`

- Tárolási fiókok listázása:

`az storage account list --resource-group {{azure_resource_group}}`

- Egy adott tárolási fiók törlése:

`az storage account delete --name {{storage_account_name}} --resource-group {{azure_resource_group}}`
