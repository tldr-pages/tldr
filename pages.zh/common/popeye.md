# popeye

> 报告 Kubernetes 部署清单中可能存在的问题。
> 更多信息：<https://github.com/derailed/popeye>.

- 扫描当前的 Kubernetes 集群：

`popeye`

- 扫描特定的命名空间：

`popeye -n {{namespace}}`

- 扫描特定的 Kubernetes 上下文：

`popeye --context={{context}}`

- 使用 spinach 配置文件进行扫描：

`popeye -f {{spinach.yaml}}`