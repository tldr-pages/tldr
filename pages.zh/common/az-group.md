# az group

> 管理资源组和模板部署。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/group>.

- 创建一个新的资源组：

`az group create {{[-n|--name]}} {{名称}} {{[-l|--location]}} {{位置}}`

- 检查资源组是否存在：

`az group exists {{[-n|--name]}} {{名称}}`

- 删除一个资源组：

`az group delete {{[-n|--name]}} {{名称}}`

- 等待资源组满足某个条件：

`az group wait {{[-n|--name]}} {{名称}} --{{created|deleted|exists|updated}}`
