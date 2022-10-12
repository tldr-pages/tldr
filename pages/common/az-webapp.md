# az webapp

> Manage Web Applications hosted in Azure Cloud Services.
> Part of `azure-cli`.
> Mode information: <https://learn.microsoft.com/cli/azure/webapp>.

- List available runtimes for a webapp:

`az webapp -list-runtimes --os-type {{windows|linux}}`

- Create a web app:

`az webapp up --name {{app_name}} --location {{location}} --runtime {{runtime}}`

- List all web apps:

`az webapp list`

- Delete a web app:

`az webapp delete --name {{app_name}} --resource-group {{resource_group}}`
