# kubectl scale

> 为部署、副本集、复制控制器或有状态集设置新大小。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#scale>。

- 扩展副本集：

`kubectl scale --replicas={{number_of_replicas}} rs/{{replica_name}}`

- 根据文件扩展资源：

`kubectl scale --replicas={{number_of_replicas}} -f {{path/to/file.yml}}`

- 根据当前副本数量扩展部署：

`kubectl scale --current-replicas={{current_replicas}} --replicas={{number_of_replicas}} deployment/{{deployment_name}}`