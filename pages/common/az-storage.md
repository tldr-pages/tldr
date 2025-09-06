# az storage

> Manage Azure Cloud Storage resources.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/storage>.

- Create a storage account specifying a location:

`az storage account create {{[-g|--resource-group]}} {{group_name}} {{[-n|--name]}} {{account_name}} {{[-l|--location]}} {{location}} --sku {{account_sku}}`

- List all storage accounts in a resource group:

`az storage account list {{[-g|--resource-group]}} {{group_name}}`

- List the access keys for a storage account:

`az storage account keys list {{[-g|--resource-group]}} {{group_name}} {{[-n|--name]}} {{account_name}}`

- Delete a storage account:

`az storage account delete {{[-g|--resource-group]}} {{group_name}} {{[-n|--name]}} {{account_name}}`

- Update the minimum tls version setting for a storage account:

`az storage account update --min-tls-version {{TLS1_0|TLS1_1|TLS1_2}} {{[-g|--resource-group]}} {{group_name}} {{[-n|--name]}} {{account_name}}`
