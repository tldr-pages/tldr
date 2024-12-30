# az 存储 blob

> 管理 Azure 中的 blob 存储容器和对象。
> 作为 `azure-cli` 的一部分（也称为 `az`）。
> 更多信息请访问：<https://learn.microsoft.com/cli/azure/storage/blob>。

- 将 blob 下载到指定的 [f]ile 路径，指定 [s]ource 容器：

`az storage blob download --account-name {{storage_account_name}} --account-key {{storage_account_key}} -c {{container_name}} -n {{path/to/blob}} -f {{path/to/local_file}}`

- 从 blob 容器递归下载 blobs：

`az storage blob download-batch --account-name {{storage_account_name}} --account-key {{storage_account_key}} -s {{container_name}} -d {{path/to/remote}} --pattern {{filename_regex}} --destination {{path/to/destination}}`

- 将本地文件上传到 blob 存储：

`az storage blob upload --account-name {{storage_account_name}} --account-key {{storage_account_key}} -c {{container_name}} -n {{path/to/blob}} -f {{path/to/local_file}}`

- 删除 blob 对象：

`az storage blob delete --account-name {{storage_account_name}} --account-key {{storage_account_key}} -c {{container_name}} -n {{path/to/blob}}`

- 为 blob 生成共享访问签名：

`az storage blob generate-sas --account-name {{storage_account_name}} --account-key {{storage_account_key}} -c {{container_name}} -n {{path/to/blob}} --permissions {{permission_set}} --expiry {{Y-m-d'T'H:M'Z'}} --https-only`