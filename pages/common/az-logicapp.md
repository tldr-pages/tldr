# az logicapp

> Manage Logic Apps in Azure Cloud Services.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/logicapp>.

- Create a logic app:

`az logicapp create --name {{name}} --resource-group {{resource_group}} --storage-account {{storage_account}}`

- Delete a logic app:

`az logicapp delete --name {{name}} --resource-group {{resource_group}}`

- List logic apps:

`az logicapp list --resource-group {{resource_group}}`

- Restart a logic app:

`az logicapp restart --name {{name}} --resource-group {{resource_group}}`

- Start a logic app:

`az logicapp start --name {{name}} --resource-group {{resource_group}}`

- Stop a logic app:

`az logicapp stop --name {{name}} --resource-group {{resource_group}}`
