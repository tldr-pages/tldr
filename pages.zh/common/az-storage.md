# az storage

> 管理 Azure Cloud Storage 资源。
> 是 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/storage>.

- 创建存储帐户并指定位置：

`az storage account create {{[-g|--resource-group]}} {{group_name}} {{[-n|--name]}} {{account_name}} {{[-l|--location]}} {{location}} --sku {{account_sku}}`

- 列出资源组中的所有存储帐户：

`az storage account list {{[-g|--resource-group]}} {{group_name}}`

- 列出存储帐户的访问密钥：

`az storage account keys list {{[-g|--resource-group]}} {{group_name}} {{[-n|--name]}} {{account_name}}`

- 删除存储帐户：

`az storage account delete {{[-g|--resource-group]}} {{group_name}} {{[-n|--name]}} {{account_name}}`

- 更新存储帐户的最小 TLS 版本设置：

`az storage account update --min-tls-version {{TLS1_0|TLS1_1|TLS1_2}} {{[-g|--resource-group]}} {{group_name}} {{[-n|--name]}} {{account_name}}`