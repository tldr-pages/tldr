# aws s3 presign

> 生成 Amazon S3 对象的预签名 URL。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/presign.html>.

- 生成特定 S3 对象的有效一小时的预签名 URL：

`aws s3 presign s3://{{bucket_name}}/{{path/to/file}}`

- 生成特定有效期的预签名 URL：

`aws s3 presign s3://{{bucket_name}}/{{path/to/file}} --expires-in {{duration_in_seconds}}`

- 显示帮助：

`aws s3 presign help`
