# az storage entity

> 管理 Azure 表存储实体。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/storage/entity>.

- 将一个实体插入到表中：

`az storage entity insert {{[-e|--entity]}} {{以空格分隔的键值对}} {{[-t|--table-name]}} {{表名}} --account-name {{存储账户名称}} --account-key {{存储账户密钥}}`

- 从表中删除一个现有实体：

`az storage entity delete --partition-key {{分区键}} --row-key {{行键}} {{[-t|--table-name]}} {{表名}} --account-name {{存储账户名称}} --account-key {{存储账户密钥}}`

- 通过合并其属性来更新一个现有实体：

`az storage entity merge {{[-e|--entity]}} {{以空格分隔的键值对}} {{[-t|--table-name]}} {{表名}} --account-name {{存储账户名称}} --account-key {{存储账户密钥}}`

- 列出满足查询条件的实体：

`az storage entity query --filter {{查询过滤条件}} {{[-t|--table-name]}} {{表名}} --account-name {{存储账户名称}} --account-key {{存储账户密钥}}`

- 从指定表中获取一个实体：

`az storage entity show --partition-key {{分区键}} --row-key {{行键}} {{[-t|--table-name]}} {{表名}} --account-name {{存储账户名称}} --account-key {{存储账户密钥}}`
