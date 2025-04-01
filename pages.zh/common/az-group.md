# az group

> 管理资源组和模板部署。
> 作为 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/group>.

- 创建一个新的资源组：

`az group create --name {{name}} --location {{location}}`

- 检查资源组是否存在：

`az group exists --name {{name}}`

- 删除资源组：

`az group delete --name {{name}}`

- 等待资源组满足某个条件：

`az group wait --name {{name}} --{{created|deleted|exists|updated}}`
