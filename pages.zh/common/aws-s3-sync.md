# aws s3 sync

> 递归地在本地系统和 S3 存储桶之间，或 S3 存储桶之间同步文件和目录。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/sync.html>.

- 从本地同步文件和目录到存储桶：

`aws s3 sync {{path/to/file_or_directory}} s3://{{bucket_target_name}}/{{path/to/remote_location}}`

- 从存储桶同步文件和目录到本地：

`aws s3 sync s3://{{bucket_source_name}}/{{path/to/remote_location}} {{path/to/file_or_directory}}`

- 在两个存储桶之间同步对象：

`aws s3 sync s3://{{bucket_source_name}}/{{path/to/remote_location}} s3://{{bucket_target_name}}/{{path/to/remote_location}}`

- 同步本地文件到 S3，同时排除特定的文件或目录：

`aws s3 sync {{path/to/file_or_directory}} s3://{{bucket_target_name}}/{{path/to/remote_location}} --exclude {{path/to/file}} --exclude {{path/to/directory}}/*`

- 在存储桶之间同步对象，并删除目标中不在源中的文件：

`aws s3 sync s3://{{bucket_source_name}}/{{path/to/remote_location}} s3://{{bucket_target_name}}/{{path/to/remote_location}} --delete`

- 以高级选项（设置 ACL 和存储类）同步到 S3：

`aws s3 sync {{path/to/local_directory}} s3://{{bucket_name}}/{{path/to/remote_location}} --acl {{private|public-read}} --storage-class {{STANDARD_IA|GLACIER}}`

- 同步文件到 S3 并跳过未更改的文件（比较大小和修改时间）：

`aws s3 sync {{path/to/file_or_directory}} s3://{{bucket_name}}/{{path/to/remote_location}} --size-only`

- 显示帮助信息：

`aws s3 sync help`