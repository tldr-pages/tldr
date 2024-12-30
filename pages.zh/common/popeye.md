# popeye

> 报告Kubernetes部署清单的潜在问题。
> 更多信息：<https://github.com/derailed/popeye>。

- 扫描当前的Kubernetes集群：

`popeye`

- 扫描特定的命名空间：

`popeye -n {{namespace}}`

- 扫描特定的Kubernetes上下文：

`popeye --context={{context}}`

- 使用菠菜配置文件进行扫描：

`popeye -f {{spinach.yaml}}`