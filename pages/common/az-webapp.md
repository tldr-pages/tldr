# az webapp

> Manage Web Applications hosted in Azure Cloud Services.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/webapp>.

- List available runtimes for a web application:

`az webapp list-runtimes {{[-os|--os-type]}} {{windows|linux}}`

- Create a web application:

`az webapp up {{[-n|--name]}} {{name}} {{[-l|--location]}} {{location}} {{[-r|--runtime]}} {{runtime}}`

- List all web applications:

`az webapp list`

- Delete a specific web application:

`az webapp delete {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`
