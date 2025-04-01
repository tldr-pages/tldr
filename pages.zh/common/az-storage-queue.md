# az storage queue

> 管理 Azure 中的存储队列。
> 属于 `azure-cli`（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/storage/queue>.

- 创建一个队列：

`az storage queue create --account-name {{storage_account_name}} --name {{queue_name}} --metadata {{queue_metadata}}`

- 为队列生成共享访问签名：

`az storage queue generate-sas --account-name {{storage_account_name}} --name {{queue_name}} --permissions {{queue_permissions}} --expiry {{expiry_date}} --https-only`

- 列出存储账户中的队列：

`az storage queue list --prefix {{filter_prefix}} --account-name {{storage_account_name}}`

- 删除指定的队列及其包含的所有消息：

`az storage queue delete --account-name {{storage_account_name}} --name {{queue_name}} --fail-not-exist`
