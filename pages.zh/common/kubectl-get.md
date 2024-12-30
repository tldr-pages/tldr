# kubectl get

> 获取 Kubernetes 对象和资源。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get>。

- 获取当前集群中的所有命名空间：

`kubectl get namespaces`

- 获取指定 [n]amespace 中的节点：

`kubectl get nodes --namespace {{namespace}}`

- 获取指定 [n]amespace 中的 pods：

`kubectl get pods --namespace {{namespace}}`

- 获取指定 [n]amespace 中的部署：

`kubectl get deployments --namespace {{namespace}}`

- 获取指定 [n]amespace 中的服务：

`kubectl get services --namespace {{namespace}}`

- 获取指定 [n]amespace 中的所有资源：

`kubectl get all --namespace {{namespace}}`

- 获取在 YAML 清单 [f]ile 中定义的 Kubernetes 对象：

`kubectl get --file {{path/to/manifest.yaml}}`