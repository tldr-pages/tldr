# kubectl label

> 标签化 Kubernetes 资源。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#label>。

- 给 Pod 添加标签：

`kubectl label pod {{pod_name}} {{key}}={{value}}`

- 通过覆盖现有值来更新 Pod 的标签：

`kubectl label --overwrite pod {{pod_name}} {{key}}={{value}}`

- 给命名空间中的所有 Pod 添加标签：

`kubectl label pods --all {{key}}={{value}}`

- 给由 Pod 定义文件标识的 Pod 添加标签：

`kubectl label -f {{pod_definition_file}} {{key}}={{value}}`

- 从 Pod 中移除标签：

`kubectl label pod {{pod_name}} {{key}}-`