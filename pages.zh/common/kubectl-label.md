# kubectl 标签

> 给 Kubernetes 资源打标签。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#label>。

- 给一个 pod 打标签：

`kubectl label pod {{pod_name}} {{key}}={{value}}`

- 通过覆盖现有值来更新 pod 标签：

`kubectl label --overwrite pod {{pod_name}} {{key}}={{value}}`

- 给命名空间中的所有 pod 打标签：

`kubectl label pods --all {{key}}={{value}}`

- 根据 pod 定义文件给 pod 打标签：

`kubectl label -f {{pod_definition_file}} {{key}}={{value}}`

- 从 pod 中移除标签：

`kubectl label pod {{pod_name}} {{key}}-`