# kubectl delete

> 删除 Kubernetes 资源。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete>。

- 删除特定的 Pod：

`kubectl delete pod {{pod_name}}`

- 删除特定的 Deployment：

`kubectl delete deployment {{deployment_name}}`

- 删除特定的 Node：

`kubectl delete node {{node_name}}`

- 删除指定命名空间中的所有 Pod：

`kubectl delete pods --all --namespace {{namespace}}`

- 删除指定命名空间中的所有 Deployment 和 Service：

`kubectl delete deployments,services --all --namespace {{namespace}}`

- 删除所有 Node：

`kubectl delete nodes --all`

- 删除 YAML 清单定义的资源：

`kubectl delete --filename {{path/to/manifest.yaml}}`