# k9s

> View and manage Kubernetes clusters.
> More information: <https://k9scli.io/topics/commands/>.

- Manage a cluster using a kubeconfig context:

`k9s --context {{kubeconfig_context_name}}`

- Manage a cluster in read-only mode (disabling all commands that may cause modifications):

`k9s --readonly --cluster {{cluster_name}}`

- Manage a cluster using a given kubernetes namespace:

`k9s --namespace {{kubernetes_namespace}} --cluster {{cluster_name}}`

- Manage a cluster launching k9s in the pod view and enable debug logging:

`k9s --command {{pod}} --logLevel debug --cluster {{cluster_name}}`
