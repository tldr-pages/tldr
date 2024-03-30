# az storage account

> Manage storage accounts in Azure.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/storage/account>.

- Create an storage account:

`az storage account create --name {{storage_account_name}} --resource-group {{azure_resource_group}} --location {{azure_location}} --sku {{storage_account_sku}}`

- Generate a shared access signature for a specific storage account:

`az storage account generate-sas --account-name {{storage_account_name}} --name {{account_name}} --permissions {{sas_permissions}} --expiry {{expiry_date}} --services {{storage_services}} --resource-types {{resource_types}}`

- List storage accounts:

`az storage account list --resource-group {{azure_resource_group}}`

- Delete a specific storage account:

`az storage account delete --name {{storage_account_name}} --resource-group {{azure_resource_group}}`
