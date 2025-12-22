# az storage

> 管理 Azure 云存储资源。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/storage>.

- 创建一个存储帐户并指定位置：

`az storage account create {{[-g|--resource-group]}} {{资源组名称}} {{[-n|--name]}} {{帐户名称}} {{[-l|--location]}} {{位置}} --sku {{帐户 SKU}}`

- 列出某个资源组中的所有存储帐户：

`az storage account list {{[-g|--resource-group]}} {{资源组名称}}`

- 列出某个存储帐户的访问密钥：

`az storage account keys list {{[-g|--resource-group]}} {{资源组名称}} {{[-n|--name]}} {{帐户名称}}`

- 删除一个存储帐户：

`az storage account delete {{[-g|--resource-group]}} {{资源组名称}} {{[-n|--name]}} {{帐户名称}}`

- 更新某个存储帐户的最低 TLS 版本设置：

`az storage account update --min-tls-version {{TLS1_0|TLS1_1|TLS1_2}} {{[-g|--resource-group]}} {{资源组名称}} {{[-n|--name]}} {{帐户名称}}`
