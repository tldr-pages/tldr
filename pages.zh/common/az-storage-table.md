# az storage table

> 在 Azure 中管理 NoSQL 键值存储。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/storage/table>.

- 在存储账户中创建一个新表：

`az storage table create --account-name {{存储账户名称}} {{[-n|--name]}} {{表名称}} --fail-on-exist`

- 为表生成共享访问签名（Shared Access Signature，SAS）：

`az storage table generate-sas --account-name {{存储账户名称}} {{[-n|--name]}} {{表名称}} --permissions {{SAS 权限}} --expiry {{过期日期}} --https-only`

- 列出存储账户中的所有表：

`az storage table list --account-name {{存储账户名称}}`

- 删除指定的表及其包含的所有数据：

`az storage table delete --account-name {{存储账户名称}} {{[-n|--name]}} {{表名称}} --fail-not-exist`
