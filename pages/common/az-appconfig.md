# az appconfig

Manage App configurations on Azure. Part of `azure-cli`. More information: <https://docs.microsoft.com/en-us/cli/azure/appconfig?view=azure-cli-latest>

- Create an App Configuration:

`az appconfig create -g {{rg_name}} --name {{appconfig_name}} -l {{location}}`

- Delete an App Configuration:

`az appconfig delete -g {{rg_name}} --name {{appconfig_name}}`

- List all App Configurations under the current subscription:

`az appconfig list`

- List all App Configurations under a resource group:

`az appconfig list -g {{rg_name}}`

- Show properties of an App Configuration:

`az appconfig show --name {{appconfig_name}}`

- Update an App Configuration:

`az appconfig update -g {{rg_name}} --name {{appconfig_name}}`