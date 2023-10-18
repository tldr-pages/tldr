# az acr

> Manage private registries with Azure Container Registries.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/acr>.

- Create a managed container registry:

`az acr create --name {{registry_name}} --resource-group {{resource_group}} --sku {{sku}}`

- Login to a registry:

`az acr login --name {{registry_name}}`

- Tag a local image for ACR:

`docker tag {{image_name}} {{registry_name}}.azurecr.io/{{image_name}}:{{tag}}`

- Push an image to a registry:

`docker push {{registry_name}}.azurecr.io/{{image_name}}:{{tag}}`

- Pull an image from a registry:

`docker pull {{registry_name}}.azurecr.io/{{image_name}}:{{tag}}`

- Delete an image from a registry:

`az acr repository delete --name {{registry_name}} --repository {{image_name}}:{{tag}}`

- Delete a managed container registry:

`az acr delete --name {{registry_name}} --resource-group {{resource_group}} --yes`

- List images within a registry:

`az acr repository list --name {{registry_name}} --output table`
