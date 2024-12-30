# kubectl 删除

> 删除 Kubernetes 资源。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete>。

- 删除特定的 Pod：

`kubectl delete pod {{pod_name}}`

- 删除特定的部署：

`kubectl delete deployment {{deployment_name}}`

- 删除特定的节点：

`kubectl delete node {{node_name}}`

- 删除指定命名空间中的所有 Pod：

`kubectl delete pods --all --namespace {{namespace}}`

- 删除指定命名空间中的所有部署和服务：

`kubectl delete deployments,services --all --namespace {{namespace}}`

- 删除所有节点：

`kubectl delete nodes --all`

- 删除 YAML 清单中定义的资源：

`kubectl delete --filename {{path/to/manifest.yaml}}`