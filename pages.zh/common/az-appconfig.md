# az appconfig

> 管理 Azure 上的应用配置。
> 属于 `azure-cli`（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/appconfig>。

- 创建一个应用配置：

`az appconfig create --name {{name}} --resource-group {{group_name}} --location {{location}}`

- 删除特定的应用配置：

`az appconfig delete --resource-group {{rg_name}} --name {{appconfig_name}}`

- 列出当前订阅下的所有应用配置：

`az appconfig list`

- 列出特定资源组下的所有应用配置：

`az appconfig list --resource-group {{rg_name}}`

- 显示应用配置的属性：

`az appconfig show --name {{appconfig_name}}`

- 更新特定的应用配置：

`az appconfig update --resource-group {{rg_name}} --name {{appconfig_name}}`