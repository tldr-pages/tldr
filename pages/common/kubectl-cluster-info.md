# kubectl cluster-info

> Display endpoint information about the Kubernetes master and services in the cluster.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_cluster-info/>.

- Show basic cluster information:

`kubectl cluster-info`

- Dump current cluster state to standard output (for debugging):

`kubectl cluster-info dump`

- Dump cluster state to a directory:

`kubectl cluster-info dump --output-directory {{path/to/directory}}`

- Use a specific kubeconfig context:

`kubectl cluster-info --context {{context_name}}`
