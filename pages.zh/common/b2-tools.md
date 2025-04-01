# b2-tools

> 轻松访问 Backblaze B2 云存储的所有功能。
> 更多信息：<https://www.backblaze.com/docs/cloud-storage-command-line-tools>.

- 登录您的账户：

`b2 authorize_account {{key_id}}`

- 列出账户中的现有存储桶：

`b2 list_buckets`

- 创建一个存储桶，提供存储桶名称和访问类型（例如 allPublic 或 allPrivate）：

`b2 create_bucket {{bucket_name}} {{allPublic|allPrivate}}`

- 上传文件。选择文件、存储桶和文件夹：

`b2 upload_file {{bucket_name}} {{path/to/file}} {{folder_name}}`

- 将源目录同步到 Backblaze B2 存储桶：

`b2 sync {{path/to/source_file}} {{bucket_name}}`

- 从一个存储桶复制文件到另一个存储桶：

`b2 copy-file-by-id {{path/to/source_file_id}} {{destination_bucket_name}} {{path/to/b2_file}}`

- 显示存储桶中的文件：

`b2 ls {{bucket_name}}`

- 删除匹配特定模式的“文件夹”或一组文件：

`b2 rm {{path/to/folder|pattern}}`
