# az 存储帐户

> 管理 Azure 中的存储帐户。
> 是 `azure-cli` 的一部分（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/storage/account>。

- 创建一个存储帐户：

`az storage account create --name {{storage_account_name}} --resource-group {{azure_resource_group}} --location {{azure_location}} --sku {{storage_account_sku}}`

- 为特定存储帐户生成共享访问签名：

`az storage account generate-sas --account-name {{storage_account_name}} --name {{account_name}} --permissions {{sas_permissions}} --expiry {{expiry_date}} --services {{storage_services}} --resource-types {{resource_types}}`

- 列出存储帐户：

`az storage account list --resource-group {{azure_resource_group}}`

- 删除特定存储帐户：

`az storage account delete --name {{storage_account_name}} --resource-group {{azure_resource_group}}`