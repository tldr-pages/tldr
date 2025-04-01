# aws s3 ls

> 列出 AWS S3 存储桶、文件夹（前缀）和文件（对象）。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/ls.html>.

- 列出所有存储桶：

`aws s3 ls`

- 列出存储桶根目录中的文件和文件夹（`s3://` 可选）：

`aws s3 ls s3://{{bucket_name}}`

- 列出目录中的文件和文件夹：

`aws s3 ls {{bucket_name}}/{{path/to/directory}}/`

- 列出存储桶中的所有文件：

`aws s3 ls --recursive {{bucket_name}}`

- 列出指定路径下带有前缀的所有文件：

`aws s3 ls --recursive {{bucket_name}}/{{path/to/directory/}}{{prefix}}`

- 显示帮助信息：

`aws s3 ls help`
