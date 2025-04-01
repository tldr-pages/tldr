# kind

> 使用 Docker 容器“节点”运行本地 Kubernetes 集群。
> 用于测试 Kubernetes 本身，但也可用于本地开发或持续集成。
> 更多信息：<https://github.com/kubernetes-sigs/kind>.

- 创建本地 Kubernetes 集群：

`kind create cluster --name {{cluster_name}}`

- 删除一个或多个集群：

`kind delete clusters {{cluster_name}}`

- 获取集群、节点或 kubeconfig 的详细信息：

`kind get {{clusters|nodes|kubeconfig}}`

- 导出 kubeconfig 或日志：

`kind export {{kubeconfig|logs}}`