# kind

> 使用 Docker 容器 "节点" 运行本地 Kubernetes 集群。
> 旨在测试 Kubernetes 本身，但也可以用于本地开发或持续集成。
> 更多信息请访问：<https://github.com/kubernetes-sigs/kind>。

- 创建一个本地 Kubernetes 集群：

`kind create cluster --name {{cluster_name}}`

- 删除一个或多个集群：

`kind delete clusters {{cluster_name}}`

- 获取有关集群、节点或 kubeconfig 的详细信息：

`kind get {{clusters|nodes|kubeconfig}}`

- 导出 kubeconfig 或日志：

`kind export {{kubeconfig|logs}}`