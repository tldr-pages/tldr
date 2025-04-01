# gcloud projects

> 管理 Google Cloud 中的项目访问策略。
> 参见：`gcloud`。
> 更多信息：<https://cloud.google.com/sdk/gcloud/reference/projects>。

- 创建一个新项目：

`gcloud projects create {{project_id|project_number}}`

- 列出所有活动项目：

`gcloud projects list`

- 显示项目的元数据：

`gcloud projects describe {{project_id}}`

- 删除项目：

`gcloud projects delete {{project_id|project_number}}`

- 向指定项目添加 IAM 策略绑定：

`gcloud projects add-iam-policy-binding {{project_id}} --member {{principal}} --role {{role}}`
