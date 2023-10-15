# az aks

> Manage Azure Kubernetes Service (AKS) clusters.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/aks>.

- List AKS clusters:

`az aks list --resource-group {{resource_group}}`

- Create a new AKS cluster:

`az aks create --resource-group {{resource_group}} --name {{name}} --node-count {{count}} --node-vm-size {{size}}`

- Delete an AKS cluster:

`az aks delete --resource-group {{resource_group}} --name {{name}}`

- Get the access credentials for an AKS cluster:

`az aks get-credentials --resource-group {{resource_group}} --name {{name}}`

- Get the upgrade versions available for an AKS cluster:

`az aks get-upgrades --resource-group {{resource_group}} --name {{name}}`
