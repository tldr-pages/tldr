# gcloud

> Google Cloud Platform 的官方命令行工具。
> 注意：`gcloud` 子命令有自己的使用文档。
> 更多信息：<https://cloud.google.com/sdk/gcloud>.

- 列出当前配置中的所有属性：

`gcloud config list`

- 登录到 Google 账户：

`gcloud auth login`

- 设置活动项目：

`gcloud config set project {{project_name}}`

- 登录到虚拟机实例：

`gcloud compute ssh {{user}}@{{instance}}`

- 列出项目中的所有 Google Compute Engine 实例（默认列出所有区域的实例）：

`gcloud compute instances list`

- 使用适当凭据更新 kubeconfig 文件，使 `kubectl` 指向 Google Kubernetes Engine (GKE) 中的特定集群：

`gcloud container clusters get-credentials {{cluster_name}}`

- 更新所有 `gcloud` 组件：

`gcloud components update`

- 显示给定命令的帮助信息：

`gcloud help {{command}}`
