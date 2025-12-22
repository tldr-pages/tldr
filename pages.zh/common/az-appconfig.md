# az appconfig

> 管理 Azure 上的 App Configuration。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/appconfig>.

- 创建一个 App Configuration：

`az appconfig create {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{group_name}} {{[-l|--location]}} {{location}}`

- 删除一个指定的 App Configuration：

`az appconfig delete {{[-g|--resource-group]}} {{rg_name}} {{[-n|--name]}} {{appconfig_name}}`

- 列出当前订阅下的所有 App Configuration：

`az appconfig list`

- 列出指定资源组下的所有 App Configuration：

`az appconfig list {{[-g|--resource-group]}} {{rg_name}}`

- 显示一个 App Configuration 的属性：

`az appconfig show {{[-n|--name]}} {{appconfig_name}}`

- 更新一个指定的 App Configuration：

`az appconfig update {{[-g|--resource-group]}} {{rg_name}} {{[-n|--name]}} {{appconfig_name}}`
