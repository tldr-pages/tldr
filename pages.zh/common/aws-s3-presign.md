# aws s3 presign

> 为 Amazon S3 对象生成预签名 URL。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/s3/presign.html>.

- 为指定的 S3 对象生成一个有效期为 1 小时的预签名 URL：

`aws s3 presign s3://{{存储桶名称}}/{{路径/到/文件}}`

- 生成一个具有指定有效期的预签名 URL：

`aws s3 presign s3://{{存储桶名称}}/{{路径/到/文件}} --expires-in {{持续时间（秒）}}`

- 显示帮助信息：

`aws s3 presign help`
