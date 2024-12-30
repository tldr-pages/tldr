# gsutil

> 访问 Google Cloud Storage。
> 您可以使用 `gsutil` 执行广泛的桶和对象管理任务。
> 更多信息：<https://cloud.google.com/storage/docs/gsutil>。

- 列出您已登录的项目中的所有桶：

`gsutil ls`

- 列出桶中的对象：

`gsutil ls -r 'gs://{{bucket_name}}/{{prefix}}**'`

- 从桶中下载对象：

`gsutil cp gs://{{bucket_name}}/{{object_name}} {{path/to/save_location}}`

- 上传对象到桶：

`gsutil cp {{object_location}} gs://{{destination_bucket_name}}/`

- 重命名或移动桶中的对象：

`gsutil mv gs://{{bucket_name}}/{{old_object_name}} gs://{{bucket_name}}/{{new_object_name}}`

- 在您已登录的项目中创建一个新桶：

`gsutil mb gs://{{bucket_name}}`

- 删除一个桶并移除其中的所有对象：

`gsutil rm -r gs://{{bucket_name}}`