# az storage queue

> 管理 Azure 中的存储队列。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/storage/queue>.

- 创建一个队列：

`az storage queue create --account-name {{存储账户名称}} {{[-n|--name]}} {{队列名称}} --metadata {{队列元数据}}`

- 为队列生成共享访问签名（SAS）：

`az storage queue generate-sas --account-name {{存储账户名称}} {{[-n|--name]}} {{队列名称}} --permissions {{队列权限}} --expiry {{过期日期}} --https-only`

- 列出存储账户中的队列：

`az storage queue list --prefix {{过滤前缀}} --account-name {{存储账户名称}}`

- 删除指定的队列及其包含的所有消息：

`az storage queue delete --account-name {{存储账户名称}} {{[-n|--name]}} {{队列名称}} --fail-not-exist`
