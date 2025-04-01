# az network

> 管理 Azure 网络资源。
> 作为 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/network>.

- 列出用于订阅配额的区域网络资源：

`az network list-usages`

- 列出订阅中的所有虚拟网络：

`az network vnet list`

- 创建虚拟网络：

`az network vnet create --address-prefixes {{10.0.0.0/16}} --name {{vnet}} --resource-group {{group_name}} --subnet-name {{subnet}} --subnet-prefixes {{10.0.0.0/24}}`

- 为网络接口卡启用加速网络：

`az network nic update --accelerated-networking true --name {{nic}} --resource-group {{resource_group}}`