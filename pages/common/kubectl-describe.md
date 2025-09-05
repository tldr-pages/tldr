# kubectl-describe

> Show details of Kubernetes objects.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe>.

- Show details of a specific Pod in the current namespace:

`kubectl describe pod {{pod-name}}`

- Show details of a specific Service in a given namespace:

`kubectl describe service {{service-name}} --namespace {{namespace-name}}`

- Show details of a specific Node:

`kubectl describe node {{node-name}}`

- Show details of all resources of a certain type in the current namespace:

`kubectl describe {{resource_type}}`

- Show details of Kubernetes objects defined in a YAML manifest file:

`kubectl describe {{[-f|--filename]}} {{path/to/manifest.yaml}}`
