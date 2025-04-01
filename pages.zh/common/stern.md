# stern

> 跟踪来自 Kubernetes 的多个 Pod 和容器的输出。
> 更多信息：<https://github.com/stern/stern>.

- 跟踪当前命名空间内的所有 Pod：

`stern .`

- 跟踪具有特定状态的所有 Pod：

`stern . --container-state {{running|waiting|terminated}}`

- 跟踪与给定正则表达式匹配的所有 Pod：

`stern {{pod_query}}`

- 跟踪来自所有命名空间的匹配 Pod：

`stern {{pod_query}} --all-namespaces`

- 跟踪从 15 分钟前开始的匹配 Pod：

`stern {{pod_query}} --since {{15m}}`

- 跟踪具有特定标签的匹配 Pod：

`stern {{pod_query}} --selector {{release=canary}}`
