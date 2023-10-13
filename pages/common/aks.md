# aks

> The official CLI tool for Azure Kubernetes Service (AKS).
> Manage Azure Kubernetes Service (AKS) clusters.
> Official documentation: [https://docs.microsoft.com/cli/azure/aks](https://docs.microsoft.com/cli/azure/aks).

- Create a new AKS cluster:

`az aks create --resource-group myResourceGroup --name myAKSCluster --node-count 1 --enable-addons monitoring --generate-ssh-keys`

- List AKS clusters:

`az aks list --resource-group myResourceGroup`

- Scale the node pool in an AKS cluster:

`az aks scale --resource-group myResourceGroup --name myAKSCluster --node-count 3`

- Get credentials for a managed Kubernetes cluster:

`az aks get-credentials --resource-group myResourceGroup --name myAKSCluster`

- Upgrade an AKS cluster to a newer Kubernetes version:

`az aks upgrade --resource-group myResourceGroup --name myAKSCluster --kubernetes-version 1.12.4`

- Show the details for an AKS cluster:

`az aks show --resource-group myResourceGroup --name myAKSCluster`

- Delete an AKS cluster:

`az aks delete --resource-group myResourceGroup --name myAKSCluster`

- Get the credentials for a managed Kubernetes cluster and save to a file:

`az aks get-credentials --resource-group myResourceGroup --name myAKSCluster --file myAKSCluster.kubeconfig`