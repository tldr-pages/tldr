# az aks

> 管理 Azure Kubernetes Service (AKS) 集群。
> 属于 `azure-cli`（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/aks>.

- 列出 AKS 集群：

`az aks list --resource-group {{resource_group}}`

- 创建新的 AKS 集群：

`az aks create --resource-group {{resource_group}} --name {{name}} --node-count {{count}} --node-vm-size {{size}}`

- 删除 AKS 集群：

`az aks delete --resource-group {{resource_group}} --name {{name}}`

- 获取 AKS 集群的访问凭据：

`az aks get-credentials --resource-group {{resource_group}} --name {{name}}`

- 获取 AKS 集群可用的升级版本：

`az aks get-upgrades --resource-group {{resource_group}} --name {{name}}`