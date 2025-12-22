# az storage account

> 管理 Azure 中的存储账户。
> `azure-cli` 的一部分（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/storage/account>.

- 创建一个存储账户：

`az storage account create {{[-n|--name]}} {{存储账户名称}} {{[-g|--resource-group]}} {{Azure 资源组}} --location {{Azure 区域}} --sku {{存储账户 SKU}}`

- 为指定的存储账户生成共享访问签名（SAS）：

`az storage account generate-sas --account-name {{存储账户名称}} {{[-n|--name]}} {{账户名称}} --permissions {{SAS 权限}} --expiry {{过期日期}} --services {{存储服务}} --resource-types {{资源类型}}`

- 列出存储账户：

`az storage account list {{[-g|--resource-group]}} {{Azure 资源组}}`

- 删除指定的存储账户：

`az storage account delete {{[-n|--name]}} {{存储账户名称}} {{[-g|--resource-group]}} {{Azure 资源组}}`
