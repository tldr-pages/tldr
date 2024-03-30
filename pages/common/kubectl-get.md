# kubectl get

> Get Kubernetes objects and resources.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#get>.

- Get all namespaces in the current cluster:

`kubectl get namespaces`

- Get nodes in a specified [n]amespace:

`kubectl get nodes --namespace {{namespace}}`

- Get pods in a specified [n]amespace:

`kubectl get pods --namespace {{namespace}}`

- Get deployments in a specified [n]amespace:

`kubectl get deployments --namespace {{namespace}}`

- Get services in a specified [n]amespace:

`kubectl get services --namespace {{namespace}}`

- Get all resources in a specified [n]amespace:

`kubectl get all --namespace {{namespace}}`

- Get Kubernetes objects defined in a YAML manifest [f]ile:

`kubectl get --file {{path/to/manifest.yaml}}`
