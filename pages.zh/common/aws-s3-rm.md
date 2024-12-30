# aws s3 rm

> 删除 S3 对象。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/rm.html>。

- 删除特定的 S3 对象：

`aws s3 rm s3://{{bucket_name}}/{{path/to/file}}`

- 预览特定 S3 对象的删除而不实际删除（干运行）：

`aws s3 rm s3://{{bucket_name}}/{{path/to/file}} --dryrun`

- 从特定的 S3 访问点删除对象：

`aws s3 rm s3://arn:aws:s3:{{region}}:{{account_id}}:{{access_point}}/{{access_point_name}}/{{object_key}}`

- 从存储桶中删除所有对象（清空存储桶）：

`aws s3 rm s3://{{bucket_name}} --recursive`

- 显示帮助信息：

`aws s3 rm help`