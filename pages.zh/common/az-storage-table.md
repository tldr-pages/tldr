# az storage table

> 管理 Azure 中的 NoSQL 键值存储。
> 作为 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/storage/table>.

- 在存储帐户中创建新表：

`az storage table create --account-name {{storage_account_name}} --name {{table_name}} --fail-on-exist`

- 为表生成共享访问签名：

`az storage table generate-sas --account-name {{storage_account_name}} --name {{table_name}} --permissions {{sas_permissions}} --expiry {{expiry_date}} --https-only`

- 列出存储帐户中的表：

`az storage table list --account-name {{storage_account_name}}`

- 删除指定的表及其包含的所有数据：

`az storage table delete --account-name {{storage_account_name}} --name {{table_name}} --fail-not-exist`