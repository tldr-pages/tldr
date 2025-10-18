# kubectl uncordon

> Mark one or more nodes as schedulable again (reverse of `kubectl cordon`).
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_uncordon/>.

- Make a node schedulable again:

`kubectl uncordon {{node_name}}`

- Make multiple nodes schedulable again:

`kubectl uncordon {{node_name1 node_name2 ...}}`

- Use a specific kubeconfig context when uncordoning:

`kubectl uncordon {{node_name}} --context {{context_name}}`
