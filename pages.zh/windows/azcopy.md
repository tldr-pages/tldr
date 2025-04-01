# azcopy

> 用于上传文件到 Azure 云存储帐户的文件传输工具。
> 更多信息：<https://learn.microsoft.com/azure/storage/common/storage-use-azcopy-v10>.

- 登录到 Azure 租户：

`azopy login`

- 上传本地文件：

`azcopy copy '{{path\to\source_file}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}/{{blob_name}}'`

- 上传扩展名为 `.txt` 和 `.jpg` 的文件：

`azcopy copy '{{path\to\source_directory}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}' --include-pattern '{{*.txt;*.jpg}}'`

- 在两个 Azure 存储帐户之间直接复制容器：

`azcopy copy 'https://{{source_storage_account_name}}.blob.core.windows.net/{{container_name}}' 'https://{{destination_storage_account_name}}.blob.core.windows.net/{{container_name}}'`

- 同步本地目录，并删除目标中已不存在于源中的文件：

`azcopy sync '{{path\to\source_directory}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}' --recursive --delete-destination=true`

- 显示帮助：

`azcopy --help`
