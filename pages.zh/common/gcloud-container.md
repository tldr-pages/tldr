# gcloud container

> 管理 Kubernetes 上的容器化应用程序和集群。
> 参见：`gcloud`。
> 更多信息：<https://cloud.google.com/sdk/gcloud/reference/container>。

- 将 `gcloud` 注册为 Docker 凭据助手：

`gcloud auth configure-docker`

- 创建一个集群来运行 GKE 容器：

`gcloud container clusters create {{cluster_name}}`

- 列出用于运行 GKE 容器的集群：

`gcloud container clusters list`

- 更新 kubeconfig 以使 `kubectl` 使用 GKE 集群：

`gcloud container clusters get-credentials {{cluster_name}}`

- 列出容器镜像的标签和摘要元数据：

`gcloud container images list-tags {{image}}`

- 描述一个用于运行容器的现有集群：

`gcloud container clusters describe {{cluster_name}}`
