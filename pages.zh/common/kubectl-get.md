# kubectl get

> 获取 Kubernetes 对象和资源。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get>.

- 获取当前集群中的所有命名空间：

`kubectl get namespaces`

- 获取指定命名空间中的节点：

`kubectl get nodes {{[-n|--namespace]}} {{namespace}}`

- 获取指定命名空间中的 Pod：

`kubectl get pods {{[-n|--namespace]}} {{namespace}}`

- 获取指定命名空间中的部署：

`kubectl get deployments {{[-n|--namespace]}} {{namespace}}`

- 获取指定命名空间中的服务：

`kubectl get services {{[-n|--namespace]}} {{namespace}}`

- 获取指定命名空间中的所有资源：

`kubectl get all {{[-n|--namespace]}} {{namespace}}`

- 获取 YAML 清单文件中定义的 Kubernetes 对象：

`kubectl get {{[-f|--file]}} {{path/to/manifest.yaml}}`