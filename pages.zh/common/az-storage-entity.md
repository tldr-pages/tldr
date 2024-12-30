# az 存储 实体

> 管理 Azure 表存储实体。
> 属于 `azure-cli`（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/storage/entity>。

- 向表中插入实体：

`az storage entity insert --entity {{空格分隔的键值对}} --table-name {{表名}} --account-name {{存储账户名称}} --account-key {{存储账户密钥}}`

- 从表中删除现有实体：

`az storage entity delete --partition-key {{分区键}} --row-key {{行键}} --table-name {{表名}} --account-name {{存储账户名称}} --account-key {{存储账户密钥}}`

- 通过合并属性更新现有实体：

`az storage entity merge --entity {{空格分隔的键值对}} --table-name {{表名}} --account-name {{存储账户名称}} --account-key {{存储账户密钥}}`

- 列出满足查询的实体：

`az storage entity query --filter {{查询过滤器}} --table-name {{表名}} --account-name {{存储账户名称}} --account-key {{存储账户密钥}}`

- 从指定表中获取实体：

`az storage entity show --partition-key {{分区键}} --row-key {{行键}} --table-name {{表名}} --account-name {{存储账户名称}} --account-key {{存储账户密钥}}`