# kubectl

> 用于对 Kubernetes 集群执行命令的命令行界面。
> 一些子命令（如 `run`）有其自己的使用文档。
> 更多信息：<https://kubernetes.io/docs/reference/kubectl/>.

- 列出指定资源的详细信息：

`kubectl get {{pod|service|deployment|ingress|...}} -o wide`

- 为指定的 Pod 更新标签 'unhealthy'，并设置值为 'true'：

`kubectl label pods {{name}} unhealthy=true`

- 列出所有类型的资源：

`kubectl get all`

- 显示节点或 Pod 的资源（CPU/内存/存储）使用情况：

`kubectl top {{pod|node}}`

- 打印主节点和集群服务的地址：

`kubectl cluster-info`

- 显示特定字段的解释：

`kubectl explain {{pods.spec.containers}}`

- 打印 Pod 中容器或指定资源的日志：

`kubectl logs {{pod_name}}`

- 在现有 Pod 中运行命令：

`kubectl exec {{pod_name}} -- {{ls /}}`
