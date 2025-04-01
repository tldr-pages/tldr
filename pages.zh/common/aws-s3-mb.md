# aws s3 mb

> 创建 S3 存储桶。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/mb.html>.

- 创建 S3 存储桶：

`aws s3 mb s3://{{bucket_name}}`

- 在特定区域创建 S3 存储桶：

`aws s3 mb s3://{{bucket_name}} --region {{region}}`

- 显示帮助：

`aws s3 mb help`