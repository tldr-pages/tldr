# az logicapp

> 管理 Azure 云服务中的 Logic Apps。
> 作为 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/logicapp>.

- 创建一个 Logic App：

`az logicapp create --name {{name}} --resource-group {{resource_group}} --storage-account {{storage_account}}`

- 删除一个 Logic App：

`az logicapp delete --name {{name}} --resource-group {{resource_group}}`

- 列出 Logic Apps：

`az logicapp list --resource-group {{resource_group}}`

- 重启一个 Logic App：

`az logicapp restart --name {{name}} --resource-group {{resource_group}}`

- 启动一个 Logic App：

`az logicapp start --name {{name}} --resource-group {{resource_group}}`

- 停止一个 Logic App：

`az logicapp stop --name {{name}} --resource-group {{resource_group}}`
