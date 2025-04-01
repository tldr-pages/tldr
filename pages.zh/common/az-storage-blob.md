# az storage blob

> 管理 Azure 中的 Blob 存储容器和对象。
> 作为 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/storage/blob>。

- 下载 Blob 到指定的文件路径，同时指定源容器：

`az storage blob download --account-name {{storage_account_name}} --account-key {{storage_account_key}} {{[-c|--container-name]}} {{container_name}} {{[-n|--name]}} {{path/to/blob}} {{[-f|--file]}} {{path/to/local_file}}`

- 递归地从 Blob 容器下载 Blob：

`az storage blob download-batch --account-name {{storage_account_name}} --account-key {{storage_account_key}} {{[-s|--source]}} {{container_name}} {{[-d|--destination]}} {{path/to/remote}} --pattern {{filename_regex}} {{[-d|--destination]}} {{path/to/destination}}`

- 将本地文件上传到 Blob 存储：

`az storage blob upload --account-name {{storage_account_name}} --account-key {{storage_account_key}} {{[-c|--container-name]}} {{container_name}} {{[-n|--name]}} {{path/to/blob}} {{[-f|--file]}} {{path/to/local_file}}`

- 删除 Blob 对象：

`az storage blob delete --account-name {{storage_account_name}} --account-key {{storage_account_key}} {{[-c|--container-name]}} {{container_name}} {{[-n|--name]}} {{path/to/blob}}`

- 为 Blob 生成共享访问签名：

`az storage blob generate-sas --account-name {{storage_account_name}} --account-key {{storage_account_key}} {{[-c|--container-name]}} {{container_name}} {{[-n|--name]}} {{path/to/blob}} --permissions {{permission_set}} --expiry {{Y-m-d'T'H:M'Z'}} --https-only`