# aws s3 rm

> 删除 S3 对象。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/s3/rm.html>.

- 删除一个指定的 S3 对象：

`aws s3 rm s3://{{桶名}}/{{路径/到/文件}}`

- 预览删除指定的 S3 对象而不实际删除（试运行）：

`aws s3 rm s3://{{桶名}}/{{路径/到/文件}} --dryrun`

- 从指定的 S3 接入点删除一个对象：

`aws s3 rm s3://arn:aws:s3:{{区域}}:{{账号 ID}}:{{接入点}}/{{接入点名称}}/{{对象键}}`

- 删除桶中的所有对象（清空桶）：

`aws s3 rm s3://{{桶名}} --recursive`

- 显示帮助：

`aws s3 rm help`
