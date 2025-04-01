# kopia

> 快速、安全的开源备份工具。
> 支持加密、压缩、去重和增量快照。
> 更多信息：<https://kopia.io/docs/reference/command-line/>。

- 在本地文件系统中创建仓库：

`kopia repository create filesystem --path {{path/to/local_repository}}`

- 在 Amazon S3 上创建仓库：

`kopia repository create s3 --bucket {{bucket_name}} --access-key {{AWS_access_key_id}} --secret-access-key {{AWS_secret_access_key}}`

- 连接到仓库：

`kopia repository connect {{repository_type}} --path {{path/to/repository}}`

- 创建目录的快照：

`kopia snapshot create {{path/to/directory}}`

- 列出快照：

`kopia snapshot list`

- 将快照恢复到特定目录：

`kopia snapshot restore {{snapshot_id}} {{path/to/target_directory}}`

- 创建新策略：

`kopia policy set --global --keep-latest {{number_of_snapshots_to_keep}} --compression {{compression_algorithm}}`

- 从备份中忽略特定文件或文件夹：

`kopia policy set --global --add-ignore {{path/to/file_or_folder}}`
