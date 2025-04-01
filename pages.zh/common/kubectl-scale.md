# kubectl scale

> 为部署、副本集、复制控制器或有状态集设置新的规模。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#scale>.

- 调整副本集的规模：

`kubectl scale --replicas={{副本数量}} rs/{{副本集名称}}`

- 调整由文件标识的资源的规模：

`kubectl scale --replicas={{副本数量}} -f {{文件路径/文件.yml}}`

- 基于当前副本数量调整部署的规模：

`kubectl scale --current-replicas={{当前副本数量}} --replicas={{副本数量}} deployment/{{部署名称}}`