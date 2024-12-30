# azcopy

> 一个用于上传到 Azure 云存储账户的文件传输工具。
> 更多信息：<https://learn.microsoft.com/azure/storage/common/storage-use-azcopy-v10>。

- 登录到 Azure 租户：

`azcopy login`

- 上传本地文件：

`azcopy copy '{{path\to\source_file}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}/{{blob_name}}'`

- 上传扩展名为 `.txt` 和 `.jpg` 的文件：

`azcopy copy '{{path\to\source_directory}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}' --include-pattern '{{*.txt;*.jpg}}'`

- 在两个 Azure 存储账户之间直接复制容器：

`azcopy copy 'https://{{source_storage_account_name}}.blob.core.windows.net/{{container_name}}' 'https://{{destination_storage_account_name}}.blob.core.windows.net/{{container_name}}'`

- 同步本地目录，并在目标中删除源中不存在的文件：

`azcopy sync '{{path\to\source_directory}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}' --recursive --delete-destination=true`

- 显示帮助信息：

`azcopy --help`