# az storage container

> 在 Azure 中管理 Blob 存储容器。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/storage/container>.

- 在存储帐户中创建一个容器：

`az storage container create --account-name {{storage_account_name}} {{[-n|--name]}} {{container_name}} --public-access {{access_level}} --fail-on-exist`

- 为该容器生成一个共享访问签名：

`az storage container generate-sas --account-name {{storage_account_name}} {{[-n|--name]}} {{container_name}} --permissions {{sas_permissions}} --expiry {{expiry_date}} --https-only`

- 列出存储帐户中的容器：

`az storage container list --account-name {{storage_account_name}} --prefix {{filter_prefix}}`

- 将指定的容器标记为删除：

`az storage container delete --account-name {{storage_account_name}} {{[-n|--name]}} {{container_name}} --fail-not-exist`
