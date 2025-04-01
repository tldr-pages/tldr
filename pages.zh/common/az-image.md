# az image

> 管理 Azure 中的自定义虚拟机映像。
> 是 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/image>.

- 列出自定义映像所在的资源组：

`az image list --resource-group {{resource_group}}`

- 从托管磁盘或快照创建自定义映像：

`az image create --resource-group {{resource_group}} --name {{name}} --os-type {{windows|linux}} --source {{os_disk_source}}`

- 删除自定义映像：

`az image delete --name {{name}} --resource-group {{resource_group}}`

- 显示自定义映像的详细信息：

`az image show --name {{name}} --resource-group {{resource_group}}`

- 更新自定义映像：

`az image update --name {{name}} --resource-group {{resource_group}} --set {{property=value}}`