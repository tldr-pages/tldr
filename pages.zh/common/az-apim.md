# az apim

> 管理 Azure API 管理服务。
> 是 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/apim>.

- 列出资源组中的 API 管理服务实例：

`az apim list --resource-group {{resource_group}}`

- 创建一个 API 管理服务实例：

`az apim create --name {{name}} --resource-group {{resource_group}} --publisher-email {{email}} --publisher-name {{name}}`

- 删除一个 API 管理服务实例：

`az apim delete --name {{name}} --resource-group {{resource_group}}`

- 显示 API 管理服务实例的详细信息：

`az apim show --name {{name}} --resource-group {{resource_group}}`

- 更新 API 管理服务实例：

`az apim update --name {{name}} --resource-group {{resource_group}}`
