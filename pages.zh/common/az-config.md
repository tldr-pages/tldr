# az 配置

> 管理 Azure CLI 配置。
> 属于 `azure-cli`（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/config>。

- 打印所有配置：

`az config get`

- 打印特定部分的配置：

`az config get {{section_name}}`

- 设置配置：

`az config set {{configuration_name}}={{value}}`

- 取消设置配置：

`az config unset {{configuration_name}}`