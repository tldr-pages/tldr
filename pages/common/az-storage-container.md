# az storage container

> Manage blob storage containers in Azure.
> Part of `azure-cli`.
> More information: <https://learn.microsoft.com/cli/azure/storage/container>.

- Create a container in a storage account:

`az storage container create --account-name {{storage_account_name}} --name {{container_name}} --public-access {{access_level}} --fail-on-exist`

- Generate a shared access signature for the container:

`az storage container generate-sas --account-name {{storage_account_name}} --name {{container_name}} --permissions {{sas_permissions}} --expiry {{expiry_date}} --https-only`

- List containers in a storage account:

`az storage container list --account-name {{storage_account_name}} --prefix {{filter_prefix}}`

- Mark the specified container for deletion:

`az storage container delete --account-name {{storage_account_name}} --name {{container_name}} --fail-not-exist`
