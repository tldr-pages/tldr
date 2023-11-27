# az storage table

> Manage NoSQL key-value storage in Azure.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/storage/table>.

- Create a new table in the storage account:

`az storage table create --account-name {{storage_account_name}} --name {{table_name}} --fail-on-exist`

- Generate a shared access signature for the table:

`az storage table generate-sas --account-name {{storage_account_name}} --name {{table_name}} --permissions {{sas_permissions}} --expiry {{expiry_date}} --https-only`

- List tables in a storage account:

`az storage table list --account-name {{storage_account_name}}`

- Delete the specified table and any data it contains:

`az storage table delete --account-name {{storage_account_name}} --name {{table_name}} --fail-not-exist`
