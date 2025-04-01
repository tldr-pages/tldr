# kubectl config

> 管理用于通过 `kubectl` 或 Kubernetes API 访问集群的 Kubernetes 配置（kubeconfig）文件。
> 默认情况下，Kubernetes 会从 `${HOME}/.kube/config` 获取配置。
> 请参阅：`kubectx`，`kubens`。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#config>。

- 获取默认 kubeconfig 文件中的所有上下文：

`kubectl config get-contexts`

- 获取自定义 kubeconfig 文件中的所有集群/上下文/用户：

`kubectl config {{get-clusters|get-contexts|get-users}} --kubeconfig {{path/to/kubeconfig.yaml}}`

- 获取当前上下文：

`kubectl config current-context`

- 切换到另一个上下文：

`kubectl config {{use|use-context}} {{context_name}}`

- 删除集群/上下文/用户：

`kubectl config {{delete-cluster|delete-context|delete-user}} {{cluster|context|user}}`

- 永久添加自定义 kubeconfig 文件：

`export KUBECONFIG="{{$HOME.kube/config:path/to/custom/kubeconfig.yaml}}" kubectl config get-contexts`