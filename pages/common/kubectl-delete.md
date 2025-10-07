# kubectl delete

> Delete Kubernetes resources.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_delete>.

- Delete a specific pod:

`kubectl delete {{[po|pods]}} {{pod_name}}`

- Delete a specific deployment:

`kubectl delete {{[deploy|deployments]}} {{deployment_name}}`

- Delete a specific node:

`kubectl delete {{[no|nodes]}} {{node_name}}`

- Delete all pods in a specified namespace:

`kubectl delete {{[po|pods]}} --all {{[-n|--namespace]}} {{namespace}}`

- Delete all deployments and services in a specified namespace:

`kubectl delete {{[deploy|deployments]}},{{[svc|services]}} --all {{[-n|--namespace]}} {{namespace}}`

- Delete all nodes:

`kubectl delete {{[no|nodes]}} --all`

- Delete resources defined in a YAML manifest:

`kubectl delete {{[-f|--filename]}} {{path/to/manifest.yaml}}`
