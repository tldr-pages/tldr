# az storage blob

> 管理 Azure 中的 Blob 存储容器和对象。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/storage/blob>.

- 下载 Blob 到指定的文件路径，并指定源容器：

`az storage blob download --account-name {{账户名称}} --account-key {{账户密钥}} {{[-c|--container-name]}} {{容器名称}} {{[-n|--name]}} {{Blob 名称}} {{[-f|--file]}} {{路径/到/文件}}`

- 从 Blob 容器中递归下载 Blob：

`az storage blob download-batch --account-name {{账户名称}} --account-key {{账户密钥}} {{[-s|--source]}} {{容器名称}} --pattern {{文件名正则表达式}} {{[-d|--destination]}} {{路径/到/目标目录}}`

- 将本地文件上传到 Blob 存储：

`az storage blob upload --account-name {{账户名称}} --account-key {{账户密钥}} {{[-c|--container-name]}} {{容器名称}} {{[-n|--name]}} {{Blob 名称}} {{[-f|--file]}} {{路径/到/文件}}`

- 删除一个 Blob 对象：

`az storage blob delete --account-name {{账户名称}} --account-key {{账户密钥}} {{[-c|--container-name]}} {{容器名称}} {{[-n|--name]}} {{Blob 名称}}`

- 为一个 Blob 生成共享访问签名（SAS）：

`az storage blob generate-sas --account-name {{账户名称}} --account-key {{账户密钥}} {{[-c|--container-name]}} {{容器名称}} {{[-n|--name]}} {{Blob 名称}} --permissions {{权限集合}} --expiry {{Y-m-d'T'H:M'Z'}} --https-only`
