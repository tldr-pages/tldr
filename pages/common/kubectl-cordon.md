# kubectl cordon

> Mark a node as unschedulable, preventing new pods from being assigned to it.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cordon>.

- Mark a node as unschedulable:

`kubectl cordon {{node_name}}`

- Mark multiple nodes as unschedulable:

`kubectl cordon {{node_name1 node_name2 ...}}`

- Mark a node as unschedulable in a specific context:

`kubectl cordon {{node_name}} --context {{context_name}}`

- Mark nodes matching a label selector as unschedulable:

`kubectl cordon {{[-l|--selector]}} {{label_key}}={{label_value}}`

- Preview the changes without actually cordoning the nodes (dry run):

`kubectl cordon {{node_name}} --dry-run={{none|server|client}}`
