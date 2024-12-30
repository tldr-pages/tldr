# az 存储

> 管理 Azure 云存储资源。
> 是 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/storage>。

- 创建一个存储账户并指定一个 [l]ocation：

`az storage account create --resource-group {{group_name}} --name {{account_name}} -l {{location}} --sku {{account_sku}}`

- 列出资源组中的所有存储账户：

`az storage account list --resource-group {{group_name}}`

- 列出存储账户的访问密钥：

`az storage account keys list --resource-group {{group_name}} --name {{account_name}}`

- 删除一个存储账户：

`az storage account delete --resource-group {{group_name}} --name {{account_name}}`

- 更新存储账户的最低 TLS 版本设置：

`az storage account update --min-tls-version {{TLS1_0|TLS1_1|TLS1_2}} --resource-group {{group_name}} --name {{account_name}}`