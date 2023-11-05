# az apim

> Manage Azure API Management services.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/apim>.

- List API Management services within a resource group:

`az apim list --resource-group {{resource_group}}`

- Create an API Management service instance:

`az apim create --name {{name}} --resource-group {{resource_group}} --publisher-email {{email}} --publisher-name {{name}}`

- Delete an API Management service:

`az apim delete --name {{name}} --resource-group {{resource_group}}`

- Show details of an API Management service instance:

`az apim show --name {{name}} --resource-group {{resource_group}}`

- Update an API Management service instance:

`az apim update --name {{name}} --resource-group {{resource_group}}`
