# gcloud config set

> 在 Google Cloud CLI 配置中设置属性。
> 属性控制 Google Cloud CLI 的各种行为。
> 更多信息：<https://cloud.google.com/sdk/gcloud/reference/config/set>.

- 在 core 部分设置项目属性：

`gcloud config set project {{project_id}}`

- 为未来的操作设置计算区域：

`gcloud config set compute/zone {{zone_name}}`

- 禁用提示，使 gcloud 适合脚本使用：

`gcloud config set disable_prompts true`

- 查看当前正在使用的属性列表：

`gcloud config list`

- 取消设置之前设置的属性：

`gcloud config unset {{property_name}}`

- 创建新的配置文件：

`gcloud config configurations create {{configuration_name}}`

- 在不同的配置文件之间切换：

`gcloud config configurations activate {{configuration_name}}`
