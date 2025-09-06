# az group

> Manage resource groups and template deployments.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/group>.

- Create a new resource group:

`az group create {{[-n|--name]}} {{name}} {{[-l|--location]}} {{location}}`

- Check if a resource group exists:

`az group exists {{[-n|--name]}} {{name}}`

- Delete a resource group:

`az group delete {{[-n|--name]}} {{name}}`

- Wait until a condition of the resource group is met:

`az group wait {{[-n|--name]}} {{name}} --{{created|deleted|exists|updated}}`
