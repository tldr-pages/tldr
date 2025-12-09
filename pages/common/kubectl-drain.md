# kubectl drain

> Drain a node in preparation for maintenance by marking it unschedulable and evicting all pods.
> See also: `kubectl cordon`, `kubectl uncordon`.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_drain>.

- Drain a node:

`kubectl drain {{node_name}}`

- Drain a node, ignoring DaemonSet-managed pods:

`kubectl drain {{node_name}} --ignore-daemonsets`

- Drain a node and delete pods using emptyDir volumes (local data will be lost):

`kubectl drain {{node_name}} --ignore-daemonsets --delete-emptydir-data`

- Drain a node, forcing eviction of pods not managed by a controller:

`kubectl drain {{node_name}} --force`

- Drain a node with a custom grace period for pod termination:

`kubectl drain {{node_name}} --grace-period {{seconds}}`

- Drain a node, evicting only pods that match a label selector:

`kubectl drain {{node_name}} --pod-selector {{label_key}}={{label_value}}`

- Drain a node with a timeout:

`kubectl drain {{node_name}} --timeout {{duration}}`

- Preview the drain operation without actually evicting pods (dry run):

`kubectl drain {{node_name}} --dry-run={{none|server|client}}`
