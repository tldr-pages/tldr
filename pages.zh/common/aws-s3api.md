# aws s3api

> 创建和删除 Amazon S3 存储桶，并编辑存储桶属性。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html>.

- 在特定区域创建存储桶：

`aws s3api create-bucket --bucket {{bucket_name}} --region {{region}} --create-bucket-configuration LocationConstraint={{region}}`

- 删除存储桶：

`aws s3api delete-bucket --bucket {{bucket_name}}`

- 列出所有存储桶：

`aws s3api list-buckets`

- 列出存储桶中的对象，仅显示每个对象的键和大小：

`aws s3api list-objects --bucket {{bucket_name}} --query '{{Contents[].{Key: Key, Size: Size}}}'`

- 向存储桶中添加对象：

`aws s3api put-object --bucket {{bucket_name}} --key {{object_key}} --body {{path/to/file}}`

- 从存储桶中下载对象（输出文件始终是最后一个参数）：

`aws s3api get-object --bucket {{bucket_name}} --key {{object_key}} {{path/to/output_file}}`

- 将 Amazon S3 存储桶策略应用到指定的存储桶：

`aws s3api put-bucket-policy --bucket {{bucket_name}} --policy file://{{path/to/bucket_policy.json}}`

- 从指定的存储桶下载 Amazon S3 存储桶策略：

`aws s3api get-bucket-policy --bucket {{bucket_name}} --query Policy --output {{json|table|text|yaml|yaml-stream}} > {{path/to/bucket_policy}}`