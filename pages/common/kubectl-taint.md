# kubectl taint

> Update the taints on one or more nodes.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#taint>.

- Apply taint to a node:

`kubectl taint nodes {{node_name}} {{label_key}}={{label_value}}:{{effect}}`

- Remove taint from a node:

`kubectl taint nodes {{node_name}} {{label_key}}:{{effect}}-`

- Remove all taints from a node:

`kubectl taint nodes {{node_name}} {{label_key}}-`
