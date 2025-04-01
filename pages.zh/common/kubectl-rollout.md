# kubectl rollout

> 管理 Kubernetes 资源（如部署、DaemonSet 和 StatefulSet）的滚动更新。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#rollout>.

- 开始资源的滚动重启：

`kubectl rollout restart {{resource_type}}/{{resource_name}}`

- 查看资源的滚动更新状态：

`kubectl rollout status {{resource_type}}/{{resource_name}}`

- 将资源回滚到上一个修订版本：

`kubectl rollout undo {{resource_type}}/{{resource_name}}`

- 查看资源的滚动更新历史：

`kubectl rollout history {{resource_type}}/{{resource_name}}`