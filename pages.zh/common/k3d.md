# k3d

> 一个用于在 Docker 中轻松创建 k3s 集群的包装器。
> 更多信息：<https://k3d.io>。

- 创建一个集群：

`k3d cluster create {{cluster_name}}`

- 删除一个集群：

`k3d cluster delete {{cluster_name}}`

- 创建一个新的容器化 k3s 节点：

`k3d node create {{node_name}}`

- 将 Docker 中的镜像导入到 k3d 集群中：

`k3d image import {{image_name}} --cluster {{cluster_name}}`

- 创建一个新的镜像仓库：

`k3d registry create {{registry_name}}`