# kubectl

> Command line interface for running commands against Kubernetes clusters.
> More information: <https://kubernetes.io/docs/reference/kubectl/>.

- List all information about a resource with more details:

`kubectl get {{pod|service|deployment|ingress|...}} -o wide`

- Update specified pod with the label 'unhealthy' and the value 'true':

`kubectl label pods {{name}} unhealthy=true`

- List all resources with different types:

`kubectl get all`

- Display resource (CPU/Memory/Storage) usage of nodes or pods:

`kubectl top {{pod|node}}`

- Print the address of the master and cluster services:

`kubectl cluster-info`

- Display an explanation of a specific field:

`kubectl explain {{pods.spec.containers}}`

- Print the logs for a container in a pod or specified resource:

`kubectl logs {{pod_name}}`

- Run command in an existing pod:

`kubectl exec {{pod_name}} -- {{ls /}}`
