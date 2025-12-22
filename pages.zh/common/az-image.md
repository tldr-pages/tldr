# az image

> 管理 Azure 中的自定义虚拟机映像。
> `azure-cli` 的一部分（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/image>.

- 列出某个资源组下的自定义映像：

`az image list {{[-g|--resource-group]}} {{resource_group}}`

- 从托管磁盘或快照创建一个自定义映像：

`az image create {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{name}} --os-type {{windows|linux}} --source {{os_disk_source}}`

- 删除一个自定义映像：

`az image delete {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- 显示某个自定义映像的详细信息：

`az image show {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- 更新自定义映像：

`az image update {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}} --set {{property=value}}`
