# aws s3

> AWS S3 的命令行接口 - 通过网络服务接口提供存储。
> 一些子命令（如 `cp`）有自己独立的使用文档。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html>.

- 显示存储桶中的文件：

`aws s3 ls {{bucket_name}}`

- 将本地文件和目录同步到存储桶：

`aws s3 sync {{path/to/file1 path/to/file2 ...}} s3://{{bucket_name}}`

- 将存储桶中的文件和目录同步到本地：

`aws s3 sync s3://{{bucket_name}} {{path/to/target}}`

- 同步文件和目录时排除某些文件和目录：

`aws s3 sync {{path/to/file1 path/to/file2 ...}} s3://{{bucket_name}} --exclude {{path/to/file}} --exclude {{path/to/directory}}/*`

- 从存储桶中删除文件：

`aws s3 rm s3://{{bucket}}/{{path/to/file}}`

- 仅预览更改：

`aws s3 {{any_command}} --dryrun`