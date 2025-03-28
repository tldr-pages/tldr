# kubectl get

> Get Kubernetes objects and resources.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get>.

- Get all namespaces in the current cluster:

`kubectl get namespaces`

- Get nodes in a specified namespace:

`kubectl get nodes {{[-n|--namespace]}} {{namespace}}`

- Get pods in a specified namespace:

`kubectl get pods {{[-n|--namespace]}} {{namespace}}`

- Get deployments in a specified namespace:

`kubectl get deployments {{[-n|--namespace]}} {{namespace}}`

- Get services in a specified namespace:

`kubectl get services {{[-n|--namespace]}} {{namespace}}`

- Get all resources in a specified namespace:

`kubectl get all {{[-n|--namespace]}} {{namespace}}`

- Get Kubernetes objects defined in a YAML manifest file:

`kubectl get {{[-f|--file]}} {{path/to/manifest.yaml}}`
