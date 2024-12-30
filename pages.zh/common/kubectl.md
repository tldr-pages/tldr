# kubectl

> 用于在 Kubernetes 集群中运行命令的命令行界面。
> 一些子命令如 `run` 有自己的使用文档。
> 更多信息：<https://kubernetes.io/docs/reference/kubectl/>。

- 列出有关资源的更多详细信息：

`kubectl get {{pod|service|deployment|ingress|...}} -o wide`

- 将指定的 pod 更新为标签 'unhealthy' 和值 'true'：

`kubectl label pods {{name}} unhealthy=true`

- 列出所有不同类型的资源：

`kubectl get all`

- 显示节点或 pod 的资源（CPU/内存/存储）使用情况：

`kubectl top {{pod|node}}`

- 打印主节点和集群服务的地址：

`kubectl cluster-info`

- 显示特定字段的解释：

`kubectl explain {{pods.spec.containers}}`

- 打印 pod 中容器或指定资源的日志：

`kubectl logs {{pod_name}}`

- 在现有 pod 中运行命令：

`kubectl exec {{pod_name}} -- {{ls /}}`