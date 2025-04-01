# s3cmd

> S3 兼容对象存储的命令行工具和客户端，用于上传、检索和管理数据。
> 更多信息：<https://s3tools.org/s3cmd>。

- 调用配置/重新配置工具：

`s3cmd --configure`

- 列出存储桶/文件夹/对象：

`s3cmd ls s3://{{bucket|path/to/file}}`

- 创建存储桶/文件夹：

`s3cmd mb s3://{{bucket}}`

- 从存储桶下载特定文件：

`s3cmd get s3://{{bucket_name}}/{{path/to/file}} {{path/to/local_file}}`

- 上传文件到存储桶：

`s3cmd put {{local_file}} s3://{{bucket}}/{{file}}`

- 将对象移动到特定的存储桶位置：

`s3cmd mv s3://{{src_bucket}}/{{src_object}} s3://{{dst_bucket}}/{{dst_object}}`

- 删除特定对象：

`s3cmd rm s3://{{bucket}}/{{object}}`
