# az appconfig

> Manage App configurations on Azure.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/appconfig>.

- Create an App Configuration:

`az appconfig create {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{group_name}} {{[-l|--location]}} {{location}}`

- Delete a specific App Configuration:

`az appconfig delete {{[-g|--resource-group]}} {{rg_name}} {{[-n|--name]}} {{appconfig_name}}`

- List all App Configurations under the current subscription:

`az appconfig list`

- List all App Configurations under a specific resource group:

`az appconfig list {{[-g|--resource-group]}} {{rg_name}}`

- Show properties of an App Configuration:

`az appconfig show {{[-n|--name]}} {{appconfig_name}}`

- Update a specific App Configuration:

`az appconfig update {{[-g|--resource-group]}} {{rg_name}} {{[-n|--name]}} {{appconfig_name}}`
