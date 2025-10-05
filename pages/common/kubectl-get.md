# kubectl get

> Get Kubernetes objects and resources.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_get>.

- Get all namespaces in the current cluster:

`kubectl get {{[ns|namespaces]}}`

- Get nodes in a specified namespace:

`kubectl get {{[no|nodes]}} {{[-n|--namespace]}} {{namespace}}`

- Get pods in a specified namespace:

`kubectl get {{[po|pods]}} {{[-n|--namespace]}} {{namespace}}`

- Get deployments in a specified namespace:

`kubectl get {{[deploy|deployments]}} {{[-n|--namespace]}} {{namespace}}`

- Get services in a specified namespace:

`kubectl get {{[svc|services]}} {{[-n|--namespace]}} {{namespace}}`

- Get other resources:

`kubectl get {{persistentvolumeclaims|secret|...}}`

- Get all resources in all namespaces:

`kubectl get all {{[-A|--all-namespaces]}}`

- Get Kubernetes objects defined in a YAML manifest file:

`kubectl get {{[-f|--filename]}} {{path/to/manifest.yaml}}`
