# az advisor

> Manage Azure subscription information.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/advisor>.

- List Azure Advisor configuration for the entire subscription:

`az advisor configuration list`

- Show Azure Advisor configuration for the given subscription or resource group:

`az advisor configuration show --resource_group {{resource_group}}`

- List Azure Advisor recommendations:

`az advisor recommendation list`

- Enable Azure Advisor recommendations:

`az advisor recommendation enable --resource_group {{resource_group}}`

- Disable Azure Advisor recommendations:

`az advisor recommendation disable --resource_group {{resource_group}}`
