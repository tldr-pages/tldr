# az advisor

> 管理 Azure 订阅信息。
> 属于 `azure-cli`（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/advisor>.

- 列出整个订阅的 Azure 顾问配置：

`az advisor configuration list`

- 显示给定订阅或资源组的 Azure 顾问配置：

`az advisor configuration show --resource_group {{resource_group}}`

- 列出 Azure 顾问的建议：

`az advisor recommendation list`

- 启用 Azure 顾问的建议：

`az advisor recommendation enable --resource_group {{resource_group}}`

- 禁用 Azure 顾问的建议：

`az advisor recommendation disable --resource_group {{resource_group}}`