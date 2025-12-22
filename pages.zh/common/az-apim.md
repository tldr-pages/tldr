# az apim

> 管理 Azure API Management 服务。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/apim>.

- 列出资源组中的 API Management 服务：

`az apim list {{[-g|--resource-group]}} {{resource_group}}`

- 创建一个 API Management 服务实例：

`az apim create {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}} --publisher-email {{email}} --publisher-name {{name}}`

- 删除一个 API Management 服务：

`az apim delete {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- 显示 API Management 服务实例的详细信息：

`az apim show {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- 更新 API Management 服务实例：

`az apim update {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`
