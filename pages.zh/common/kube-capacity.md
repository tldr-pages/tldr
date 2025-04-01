# kube-capacity

> 提供 Kubernetes 集群中资源请求、限制和使用情况的概览。
> 结合了 `kubectl top` 和 `kubectl describe` 的最佳功能，专注于集群资源的 CLI。
> 更多信息：<https://github.com/robscott/kube-capacity>.

- 列出节点，包括总的 CPU 和内存资源请求和限制：

`kube-capacity`

- 包含 Pod：

`kube-capacity -p`

- 包含使用情况：

`kube-capacity -u`