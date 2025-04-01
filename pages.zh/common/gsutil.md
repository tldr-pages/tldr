# gsutil

> 访问 Google Cloud Storage。
> 您可以使用 `gsutil` 执行广泛的存储桶和对象管理任务。
> 更多信息：<https://cloud.google.com/storage/docs/gsutil>.

- 列出您已登录项目中的所有存储桶：

`gsutil ls`

- 列出存储桶中的对象：

`gsutil ls -r 'gs://{{bucket_name}}/{{prefix}}**'`

- 从存储桶下载对象：

`gsutil cp gs://{{bucket_name}}/{{object_name}} {{path/to/save_location}}`

- 将对象上传到存储桶：

`gsutil cp {{object_location}} gs://{{destination_bucket_name}}/`

- 在存储桶中重命名或移动对象：

`gsutil mv gs://{{bucket_name}}/{{old_object_name}} gs://{{bucket_name}}/{{new_object_name}}`

- 在您已登录的项目中创建新的存储桶：

`gsutil mb gs://{{bucket_name}}`

- 删除存储桶并移除其中的所有对象：

`gsutil rm -r gs://{{bucket_name}}`
