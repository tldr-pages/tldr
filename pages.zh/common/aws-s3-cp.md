# aws s3 cp

> 将本地文件或 S3 对象复制到另一个本地位置或 S3 中。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/cp.html>。

- 将文件从本地复制到指定的 S3 存储桶：

`aws s3 cp {{path/to/file}} s3://{{bucket_name}}/{{path/to/remote_file}}`

- 将指定的 S3 对象复制到另一个 S3 存储桶：

`aws s3 cp s3://{{bucket_name1}}/{{path/to/file}} s3://{{bucket_name2}}/{{path/to/target}}`

- 将指定的 S3 对象复制到另一个 S3 存储桶并保持原始名称：

`aws s3 cp s3://{{bucket_name1}}/{{path/to/file}} s3://{{bucket_name2}}`

- 递归地将 S3 对象复制到本地目录：

`aws s3 cp s3://{{bucket_name}} . --recursive`

- 显示帮助：

`aws s3 cp help`
