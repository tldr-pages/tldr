# kubectl delete

> Delete Kubernetes resources.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete>.

- Delete a specific pod:

`kubectl delete {{[po|pod]}} {{pod_name}}`

- Delete a specific deployment:

`kubectl delete {{[deploy|deployment]}} {{deployment_name}}`

- Delete a specific node:

`kubectl delete {{[no|node]}} {{node_name}}`

- Delete all pods in a specified namespace:

`kubectl delete {{[po|pods]}} --all {{[-n|--namespace]}} {{namespace}}`

- Delete all deployments and services in a specified namespace:

`kubectl delete {{[deploy|deployment]}},{{[svcľservices]}} --all {{[-n|--namespace]}} {{namespace}}`

- Delete all nodes:

`kubectl delete {{[no|nodes]}} --all`

- Delete resources defined in a YAML manifest:

`kubectl delete {{[-f|--filename]}} {{path/to/manifest.yaml}}`
