# gcloud

> Google Cloud Platform 的官方 CLI 工具。
> 注意：`gcloud` 子命令有其自己的使用文档。
> 更多信息：<https://cloud.google.com/sdk/gcloud>。

- 列出当前配置中的所有属性：

`gcloud config list`

- 登录到 Google 账户：

`gcloud auth login`

- 设置活动项目：

`gcloud config set project {{project_name}}`

- SSH 连接到虚拟机实例：

`gcloud compute ssh {{user}}@{{instance}}`

- 显示项目中的所有 Google Compute Engine 实例（默认情况下列出所有区域的实例）：

`gcloud compute instances list`

- 使用适当的凭据更新 kubeconfig 文件，以便将 `kubectl` 指向 Google Kubernetes Engine (GKE) 中的特定集群：

`gcloud container clusters get-credentials {{cluster_name}}`

- 更新所有 `gcloud` 组件：

`gcloud components update`

- 显示给定命令的帮助：

`gcloud help {{command}}`