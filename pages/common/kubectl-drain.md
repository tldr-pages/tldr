# kubectl drain

> Safely evict all pods from one or more nodes in preparation for maintenance.
> This command cordons the node first, then evicts pods. DaemonSet-managed and mirror pods are ignored by default.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_drain/>.

- Drain a node, respecting PodDisruptionBudgets:

`kubectl drain {{node_name}}`

- Drain a node and force delete standalone pods (not managed by a controller):

`kubectl drain {{node_name}} --force`

- Drain a node and delete pods that use `emptyDir` volumes:

`kubectl drain {{node_name}} --delete-emptydir-data`

- Drain a control-plane node (ignore DaemonSets and allow control-plane):

`kubectl drain {{node_name}} --ignore-daemonsets --force --delete-emptydir-data`

- Drain nodes selected by a label selector:

`kubectl drain --selector {{key}}={{value}}`
