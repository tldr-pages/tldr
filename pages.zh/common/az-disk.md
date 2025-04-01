# az disk

> 管理 Azure 托管磁盘。
> 是 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/disk>.

- 创建托管磁盘：

`az disk create --resource-group {{resource_group}} --name {{disk_name}} --size-gb {{size_in_gb}}`

- 列出资源组中的托管磁盘：

`az disk list --resource-group {{resource_group}}`

- 删除托管磁盘：

`az disk delete --resource-group {{resource_group}} --name {{disk_name}}`

- 授予托管磁盘读取或写入访问权限（用于导出）：

`az disk grant-access --resource-group {{resource_group}} --name {{disk_name}} --access-level {{Read|Write}} --duration-in-seconds {{seconds}}`

- 更新磁盘大小：

`az disk update --resource-group {{resource_group}} --name {{disk_name}} --size-gb {{new_size_in_gb}}`
