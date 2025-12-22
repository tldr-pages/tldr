# aws s3 rb

> 删除一个空的 Amazon S3 存储桶。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/s3/rb.html>.

- 删除一个空的 Amazon S3 存储桶：

`aws s3 rb s3://{{存储桶名称}}`

- 强制删除一个 Amazon S3 存储桶及其未启用版本控制的对象（如果存在已启用版本控制的对象将会失败）：

`aws s3 rb s3://{{存储桶名称}} --force`
