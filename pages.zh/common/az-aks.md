# az aks

> 管理 Azure Kubernetes Service（AKS）集群。
> `azure-cli` 的一部分（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/aks>.

- 列出 AKS 集群：

`az aks list {{[-g|--resource-group]}} {{资源组}}`

- 创建一个新的 AKS 集群：

`az aks create {{[-g|--resource-group]}} {{资源组}} {{[-n|--name]}} {{名称}} {{[-c|--node-count]}} {{数量}} --node-vm-size {{大小}}`

- 删除一个 AKS 集群：

`az aks delete {{[-g|--resource-group]}} {{资源组}} {{[-n|--name]}} {{名称}}`

- 获取 AKS 集群的访问凭据：

`az aks get-credentials {{[-g|--resource-group]}} {{资源组}} {{[-n|--name]}} {{名称}}`

- 获取 AKS 集群可用的升级版本：

`az aks get-upgrades {{[-g|--resource-group]}} {{资源组}} {{[-n|--name]}} {{名称}}`
