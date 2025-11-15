# kubectl describe

> Show details of Kubernetes resources.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_describe>.

- Show details of pods in a namespace:

`kubectl describe {{[po|pods]}} {{[-n|--namespace]}} {{namespace}}`

- Show details of nodes in a namespace:

`kubectl describe {{[no|nodes]}} {{[-n|--namespace]}} {{namespace}}`

- Show the details of a specific pod in a namespace:

`kubectl describe {{[po|pods]}} {{pod_name}} {{[-n|--namespace]}} {{namespace}}`

- Show the details of a specific node in a namespace:

`kubectl describe {{[no|nodes]}} {{node_name}} {{[-n|--namespace]}} {{namespace}}`

- Show details of Kubernetes objects defined in a YAML manifest file:

`kubectl describe {{[-f|--filename]}} {{path/to/manifest.yaml}}`
