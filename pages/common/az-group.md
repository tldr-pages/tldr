# az group

> Manage resource groups and template deployments.
> Part of `azure-cli`.
> More information: <https://docs.microsoft.com/cli/azure/group>.

- Create a new resource group:

`az group create --name {{name}} --location {{location}}`

- Check if a resource group exists:

`az group exists --name {{name}}`

- Delete a resource group:

`az group delete --name {{name}}`

- Wait until a condition of the resource group is met:

`az group wait --name {{name}} --{{created|deleted|exists|updated}}`
