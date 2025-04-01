# aws s3 rm

> 删除 S3 对象。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/rm.html>。

- 删除特定的 S3 对象：

`aws s3 rm s3://{{bucket_name}}/{{path/to/file}}`

- 预览特定 S3 对象的删除操作，但不实际删除（模拟运行）：

`aws s3 rm s3://{{bucket_name}}/{{path/to/file}} --dryrun`

- 从特定的 S3 访问点删除对象：

`aws s3 rm s3://arn:aws:s3:{{region}}:{{account_id}}:{{access_point}}/{{access_point_name}}/{{object_key}}`

- 删除桶中的所有对象（清空桶）：

`aws s3 rm s3://{{bucket_name}} --recursive`

- 显示帮助：

`aws s3 rm help`