# az webapp

> Manage Azure Cloud Services (Web Apps).
> Part of `azure-cli`.
> Mode information: <https://learn.microsoft.com/cli/azure/webapp>.

- List available runtimes for a webapp:

`az webapp -list-runtime --os-type {{windows|linux}}`

- Create a web app:

`az webapp up -n {{app_name}} -l {{location}} --runtime {{runtime}}`

- List all web apps:

`az webapp list`

- Delete a web app:

`az webapp delete -n {{app_name}} -g {{resource_group}}`
