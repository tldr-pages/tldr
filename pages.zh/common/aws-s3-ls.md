# aws s3 ls

> 列出 AWS S3 存储桶、文件夹（前缀）和文件（对象）。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/s3/ls.html>.

- 列出所有存储桶：

`aws s3 ls`

- 列出存储桶根目录中的文件和文件夹（`s3://` 是可选的）：

`aws s3 ls s3://{{存储桶名称}}`

- 列出某个目录中直接包含的文件和文件夹：

`aws s3 ls {{存储桶名称}}/{{路径/到/目录}}/`

- 列出存储桶中的所有文件：

`aws s3 ls --recursive {{存储桶名称}}`

- 列出指定路径下具有给定前缀的所有文件：

`aws s3 ls --recursive {{存储桶名称}}/{{路径/到/目录}}/{{前缀}}`

- 显示帮助信息：

`aws s3 ls help`
