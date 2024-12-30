# az logicapp

> 在 Azure 云服务中管理逻辑应用。
> 属于 `azure-cli`（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/logicapp>。

- 创建逻辑应用：

`az logicapp create --name {{name}} --resource-group {{resource_group}} --storage-account {{storage_account}}`

- 删除逻辑应用：

`az logicapp delete --name {{name}} --resource-group {{resource_group}}`

- 列出逻辑应用：

`az logicapp list --resource-group {{resource_group}}`

- 重启逻辑应用：

`az logicapp restart --name {{name}} --resource-group {{resource_group}}`

- 启动逻辑应用：

`az logicapp start --name {{name}} --resource-group {{resource_group}}`

- 停止逻辑应用：

`az logicapp stop --name {{name}} --resource-group {{resource_group}}`