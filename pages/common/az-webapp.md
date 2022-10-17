# az webapp

> Manage Web Applications hosted in Azure Cloud Services.
> Part of `azure-cli`.
> Mode information: <https://learn.microsoft.com/cli/azure/webapp>.

- List available runtimes for a web application:

`az webapp list-runtimes --os-type {{windows|linux}}`

- Create a web application:

`az webapp up --name {{name}} --location {{location}} --runtime {{runtime}}`

- List all web applications:

`az webapp list`

- Delete a specific web application:

`az webapp delete --name {{name}} --resource-group {{resource_group}}`
