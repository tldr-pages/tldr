# az appconfig

Manage App configurations on Azure. Part of `azure-cli`. More information: <https://docs.microsoft.com/en-us/cli/azure/appconfig?view=azure-cli-latest>

- Create an App Configuration:

`az appconfig create -g {{resourcegroup_name}} -n {{appconfiguration_name}} -l {{location}}`

- Delete an App Configuration:

`az appconfig delete -g {{resourcegroup_name}} -n {{appconfiguration_name}}`

- List all App Configurations under the current subscription:

`az appconfig list`

- List all App Configurations under a resource group:

`az appconfig list -g {{resourcegroup_name}}`

- Show properties of an App Configuration:

`az appconfig show --name {{appconfiguration_name}}`

- Update an App Configuration:

`az appconfig update -g {{resourcegroup_name}} -n {{appconfiguration_name}}`

