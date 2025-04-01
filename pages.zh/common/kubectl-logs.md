# kubectl logs

> 显示 Pod 中容器的日志。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#logs>.

- 显示单容器 Pod 的日志：

`kubectl logs {{pod_name}}`

- 显示指定容器在 Pod 中的日志：

`kubectl logs --container {{container_name}} {{pod_name}}`

- 显示 Pod 中所有容器的日志：

`kubectl logs --all-containers={{true}} {{pod_name}}`

- 实时查看 Pod 日志：

`kubectl logs --follow {{pod_name}}`

- 显示比相对时间 `10s`、`5m` 或 `1h` 更新的 Pod 日志：

`kubectl logs --since={{relative_time}} {{pod_name}}`

- 显示 Pod 中最近的 10 条日志：

`kubectl logs --tail={{10}} {{pod_name}}`

- 显示指定部署的所有 Pod 日志：

`kubectl logs deployment/{{deployment_name}}`