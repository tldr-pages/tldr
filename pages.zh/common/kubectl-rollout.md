# kubectl rollout

> 管理 Kubernetes 资源的发布（部署、守护进程集和有状态集）。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#rollout>。

- 开始对资源进行滚动重启：

`kubectl rollout restart {{resource_type}}/{{resource_name}}`

- 监视资源的滚动更新状态：

`kubectl rollout status {{resource_type}}/{{resource_name}}`

- 将资源回滚到之前的版本：

`kubectl rollout undo {{resource_type}}/{{resource_name}}`

- 查看资源的发布历史：

`kubectl rollout history {{resource_type}}/{{resource_name}}`