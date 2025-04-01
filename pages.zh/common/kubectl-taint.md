# kubectl taint

> 更新节点上的污点。
> 更多信息：<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#taint>.

- 为节点应用污点：

`kubectl taint nodes {{node_name}} {{label_key}}={{label_value}}:{{effect}}`

- 从节点移除污点：

`kubectl taint nodes {{node_name}} {{label_key}}:{{effect}}-`

- 从节点移除所有污点：

`kubectl taint nodes {{node_name}} {{label_key}}-`