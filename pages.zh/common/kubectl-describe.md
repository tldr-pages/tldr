# kubectl 描述

> 显示 Kubernetes 对象和资源的详细信息。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe>。

- 显示 [n]amespaces 中 pods 的详细信息：

`kubectl describe pods --namespace {{namespace}}`

- 显示 [n]amespaces 中 nodes 的详细信息：

`kubectl describe nodes --namespace {{namespace}}`

- 显示 [n]amespaces 中特定 pod 的详细信息：

`kubectl describe pods {{pod_name}} --namespace {{namespace}}`

- 显示 [n]amespaces 中特定 node 的详细信息：

`kubectl describe nodes {{node_name}} --namespace {{namespace}}`

- 显示在 YAML 清单 [f]ile 中定义的 Kubernetes 对象的详细信息：

`kubectl describe --file {{path/to/manifest.yaml}}`