# aws s3 mv

> 将本地文件或 S3 对象移动到本地或 S3 中的另一个位置。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/mv.html>.

- 将文件从本地移动到指定的 S3 存储桶：

`aws s3 mv {{path/to/local_file}} s3://{{bucket_name}}/{{path/to/remote_file}}`

- 将特定的 S3 对象移动到另一个存储桶：

`aws s3 mv s3://{{bucket_name1}}/{{path/to/file}} s3://{{bucket_name2}}/{{path/to/target}}`

- 将特定的 S3 对象移动到另一个存储桶并保持原始名称：

`aws s3 mv s3://{{bucket_name1}}/{{path/to/file}} s3://{{bucket_name2}}`

- 显示帮助：

`aws s3 mv help`
