# az storage entity

> 管理 Azure Table 存储实体。
> 作为 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/storage/entity>.

- 将实体插入表中：

`az storage entity insert --entity {{space_separated_key_value_pairs}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`

- 从表中删除现有实体：

`az storage entity delete --partition-key {{partition_key}} --row-key {{row_key}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`

- 通过合并属性更新现有实体：

`az storage entity merge --entity {{space_separated_key_value_pairs}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`

- 列出满足查询条件的实体：

`az storage entity query --filter {{query_filter}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`

- 从指定的表中获取实体：

`az storage entity show --partition-key {{partition_key}} --row-key {{row_key}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`
