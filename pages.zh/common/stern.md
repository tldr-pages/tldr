# stern

> 从 Kubernetes 中尾随多个 pod 和容器。
> 更多信息：<https://github.com/stern/stern>。

- 尾随当前命名空间内的所有 pod：

`stern .`

- 尾随具有特定状态的所有 pod：

`stern . --container-state {{running|waiting|terminated}}`

- 尾随与给定正则表达式匹配的所有 pod：

`stern {{pod_query}}`

- 从所有命名空间尾随匹配的 pod：

`stern {{pod_query}} --all-namespaces`

- 尾随 15 分钟前的匹配 pod：

`stern {{pod_query}} --since {{15m}}`

- 尾随具有特定标签的匹配 pod：

`stern {{pod_query}} --selector {{release=canary}}`