# aws s3api

> 创建和删除 Amazon S3 存储桶，并编辑存储桶属性。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/s3api/>.

- 在指定区域创建存储桶：

`aws s3api create-bucket --bucket {{存储桶名称}} --region {{区域}} --create-bucket-configuration LocationConstraint={{区域}}`

- 删除存储桶：

`aws s3api delete-bucket --bucket {{存储桶名称}}`

- 列出存储桶：

`aws s3api list-buckets`

- 列出存储桶中的对象，并且只显示每个对象的键和大小：

`aws s3api list-objects --bucket {{存储桶名称}} --query '{{Contents[].{Key: Key, Size: Size}}}'`

- 向存储桶添加一个对象：

`aws s3api put-object --bucket {{存储桶名称}} --key {{对象键}} --body {{路径/到/文件}}`

- 从存储桶下载对象（输出文件始终是最后一个参数）：

`aws s3api get-object --bucket {{存储桶名称}} --key {{对象键}} {{路径/到/输出文件}}`

- 将 Amazon S3 存储桶策略应用到指定的存储桶：

`aws s3api put-bucket-policy --bucket {{存储桶名称}} --policy file://{{路径/到/存储桶策略.json}}`

- 从指定的存储桶下载 Amazon S3 存储桶策略：

`aws s3api get-bucket-policy --bucket {{存储桶名称}} --query Policy --output {{json|table|text|yaml|yaml-stream}} > {{路径/到/存储桶策略}}`
