# k3d

> 一个封装工具，用于在 Docker 中轻松创建 k3s 集群。
> 更多信息：<https://k3d.io>。

- 创建一个集群：

`k3d cluster create {{cluster_name}}`

- 删除一个集群：

`k3d cluster delete {{cluster_name}}`

- 创建一个新的容器化 k3s 节点：

`k3d node create {{node_name}}`

- 从 Docker 导入镜像到 k3d 集群：

`k3d image import {{image_name}} --cluster {{cluster_name}}`

- 创建一个新的注册表：

`k3d registry create {{registry_name}}`