# az aks

> Manage Azure Kubernetes Service (AKS) clusters.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/aks>.

- List AKS clusters:

`az aks list {{[-g|--resource-group]}} {{resource_group}}`

- Create a new AKS cluster:

`az aks create {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{name}} {{[-c|--node-count]}} {{count}} --node-vm-size {{size}}`

- Delete an AKS cluster:

`az aks delete {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{name}}`

- Get the access credentials for an AKS cluster:

`az aks get-credentials {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{name}}`

- Get the upgrade versions available for an AKS cluster:

`az aks get-upgrades {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{name}}`
