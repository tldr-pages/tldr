# fluxctl

> Flux v1 的命令行工具。
> 更多信息：<https://fluxcd.io/legacy/flux/references/fluxctl>。

- 列出特定命名空间中当前运行的工作负载：

`fluxctl --k8s-fwd-ns={{namespace}} list-workloads`

- 显示已部署和可用的镜像：

`fluxctl list-images`

- 将集群与 Git 仓库同步：

`fluxctl sync`

- 为工作负载启用自动部署：

`fluxctl automate`