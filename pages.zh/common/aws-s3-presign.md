# aws s3 预签名

> 为 Amazon S3 对象生成预签名 URL。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/presign.html>。

- 为特定 S3 对象生成一个有效期为一小时的预签名 URL：

`aws s3 presign s3://{{bucket_name}}/{{path/to/file}}`

- 生成一个有效期为特定时间的预签名 URL：

`aws s3 presign s3://{{bucket_name}}/{{path/to/file}} --expires-in {{duration_in_seconds}}`

- 显示帮助：

`aws s3 presign help`