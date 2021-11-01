# az storage

> Manage Azure Cloud Storage resources.
> Part of `azure-cli`.
> More information: <https://docs.microsoft.com/cli/azure/storage>.

- Create a storage account:

`az storage account create -g {{group_name}} -n {{account_name}} -l {{location}} --sku {{account_sku}}`

- List all storage accounts in a resource group:

`az storage account list -g {{group_name}}`

- List the access keys for a storage account:

`az storage account keys list -g {{group_name}} -n {{account_name}}`

- Delete a storage account:

`az storage account delete -g {{group_name}} -n {{account_name}}`

- Update the minimum tls version setting for a storage account:

`az storage account update --min-tls-version TLS1_2 -g {{group_name}} -n {{account_name}}`
