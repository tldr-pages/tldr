# az appconfig

> Manage App configurations on Azure.
> Part of `az`.
> More information: <https://learn.microsoft.com/cli/azure/appconfig>.

- Create an App Configuration:

`az appconfig create --name {{name}} --resource-group {{group_name}} --location {{location}}`

- Delete a specific App Configuration:

`az appconfig delete --resource-group {{rg_name}} --name {{appconfig_name}}`

- List all App Configurations under the current subscription:

`az appconfig list`

- List all App Configurations under a specific resource group:

`az appconfig list --resource-group {{rg_name}}`

- Show properties of an App Configuration:

`az appconfig show --name {{appconfig_name}}`

- Update a specific App Configuration:

`az appconfig update --resource-group {{rg_name}} --name {{appconfig_name}}`
