# kubectl 日志

> 显示一个 pod 中容器的日志。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs>。

- 显示单容器 pod 的日志：

`kubectl logs {{pod_name}}`

- 显示 pod 中指定容器的日志：

`kubectl logs --container {{container_name}} {{pod_name}}`

- 显示 pod 中所有容器的日志：

`kubectl logs --all-containers={{true}} {{pod_name}}`

- 流式传输 pod 日志：

`kubectl logs --follow {{pod_name}}`

- 显示相对时间如 `10s`、`5m` 或 `1h` 之后的 pod 日志：

`kubectl logs --since={{relative_time}} {{pod_name}}`

- 显示 pod 中最近的 10 条日志：

`kubectl logs --tail={{10}} {{pod_name}}`

- 显示给定部署的所有 pod 日志：

`kubectl logs deployment/{{deployment_name}}`