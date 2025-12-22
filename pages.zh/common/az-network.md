# az network

> 管理 Azure 网络资源。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/network>.

- 列出某个区域中针对订阅配额使用的网络资源：

`az network list-usages`

- 列出订阅中的所有虚拟网络：

`az network vnet list`

- 创建一个虚拟网络：

`az network vnet create --address-prefixes {{10.0.0.0/16}} {{[-n|--name]}} {{vnet}} {{[-g|--resource-group]}} {{group_name}} --subnet-name {{subnet}} --subnet-prefixes {{10.0.0.0/24}}`

- 为网络接口卡启用加速网络：

`az network nic update --accelerated-networking true {{[-n|--name]}} {{nic}} {{[-g|--resource-group]}} {{resource_group}}`
