# kubectl uncordon

> Mark a node as schedulable, allowing new pods to be assigned to it.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_uncordon>.

- Mark a node as schedulable:

`kubectl uncordon {{node_name}}`

- Mark multiple nodes as schedulable:

`kubectl uncordon {{node_name1 node_name2 ...}}`

- Mark a node as schedulable in a specific context:

`kubectl uncordon {{node_name}} --context {{context_name}}`

- Mark nodes matching a label selector as schedulable:

`kubectl uncordon {{[-l|--selector]}} {{label_key}}={{label_value}}`

- Preview the changes without actually uncordoning the nodes (dry run):

`kubectl uncordon {{node_name}} --dry-run={{none|server|client}}`
