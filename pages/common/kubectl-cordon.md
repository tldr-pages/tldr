# kubectl cordon

> Mark one or more nodes as unschedulable (new pods won't be scheduled there).
> Use `kubectl uncordon` to make a node schedulable again.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cordon/>.

- Mark a node as unschedulable:

`kubectl cordon {{node_name}}`

- Mark multiple nodes as unschedulable:

`kubectl cordon {{node_name1 node_name2 ...}}`

- Mark a node using a specific kubeconfig context as unschedulable:

`kubectl cordon --context {{context_name}} {{node_name}}`
