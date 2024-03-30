# kubectl describe

> Show details of Kubernetes objects and resources.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe>.

- Show details of pods in a [n]amespace:

`kubectl describe pods --namespace {{namespace}}`

- Show details of nodes in a [n]amespace:

`kubectl describe nodes --namespace {{namespace}}`

- Show the details of a specific pod in a [n]amespace:

`kubectl describe pods {{pod_name}} --namespace {{namespace}}`

- Show the details of a specific node in a [n]amespace:

`kubectl describe nodes {{node_name}} --namespace {{namespace}}`

- Show details of Kubernetes objects defined in a YAML manifest [f]ile:

`kubectl describe --file {{path/to/manifest.yaml}}`
