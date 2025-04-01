# aws s3 rb

> 删除空的 S3 存储桶。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/s3/rb.html>。

- 删除空的 S3 存储桶：

`aws s3 rb s3://{{bucket_name}}`

- 强制删除 S3 存储桶及其非版本化对象（如果存在版本化对象，将会失败）：

`aws s3 rb s3://{{bucket_name}} --force`
