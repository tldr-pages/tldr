# az logicapp

> Manage Logic Apps in Azure Cloud Services.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/logicapp>.

- Create a logic app:

`az logicapp create {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}} {{[-s|--storage-account]}} {{storage_account}}`

- Delete a logic app:

`az logicapp delete {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- List logic apps:

`az logicapp list {{[-g|--resource-group]}} {{resource_group}}`

- Restart a logic app:

`az logicapp restart {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Start a logic app:

`az logicapp start {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Stop a logic app:

`az logicapp stop {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`
