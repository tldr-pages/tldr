# az storage container

> 管理 Azure 中的 Blob 存储容器。
> 属于 `azure-cli`（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/storage/container>.

- 在存储帐户中创建容器：

`az storage container create --account-name {{storage_account_name}} --name {{container_name}} --public-access {{access_level}} --fail-on-exist`

- 为容器生成共享访问签名：

`az storage container generate-sas --account-name {{storage_account_name}} --name {{container_name}} --permissions {{sas_permissions}} --expiry {{expiry_date}} --https-only`

- 列出存储帐户中的容器：

`az storage container list --account-name {{storage_account_name}} --prefix {{filter_prefix}}`

- 标记指定容器以供删除：

`az storage container delete --account-name {{storage_account_name}} --name {{container_name}} --fail-not-exist`