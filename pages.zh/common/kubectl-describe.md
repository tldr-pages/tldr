# kubectl describe

> 显示 Kubernetes 对象和资源的详细信息。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe>.

- 显示命名空间中所有 Pod 的详细信息：

`kubectl describe pods {{[-n|--namespace]}} {{namespace}}`

- 显示命名空间中所有节点的详细信息：

`kubectl describe nodes {{[-n|--namespace]}} {{namespace}}`

- 显示命名空间中特定 Pod 的详细信息：

`kubectl describe pods {{pod_name}} {{[-n|--namespace]}} {{namespace}}`

- 显示命名空间中特定节点的详细信息：

`kubectl describe nodes {{node_name}} {{[-n|--namespace]}} {{namespace}}`

- 显示 YAML 清单文件中定义的 Kubernetes 对象的详细信息：

`kubectl describe {{[-f|--file]}} {{path/to/manifest.yaml}}`