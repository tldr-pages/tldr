# k9s

> 查看和管理 Kubernetes 集群。
> 更多信息：<https://k9scli.io/topics/commands/>。

- 使用 kubeconfig 上下文管理集群：

`k9s --context {{kubeconfig_context_name}}`

- 以只读模式管理集群（禁用所有可能导致修改的命令）：

`k9s --readonly --cluster {{cluster_name}}`

- 使用指定的 Kubernetes 命名空间管理集群：

`k9s --namespace {{kubernetes_namespace}} --cluster {{cluster_name}}`

- 启动 k9s 在 pod 视图中管理集群并启用调试日志：

`k9s --command {{pod}} --logLevel debug --cluster {{cluster_name}}`