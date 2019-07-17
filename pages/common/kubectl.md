# kubectl

> Command line interface for running commands against Kubernetes clusters.
> More information: <https://kubernetes.io/docs/reference/kubectl/>.

- List all information about a resource (pods, deployments, services, ingresses, etc.) with more details:

`kubectl get pods -o wide`

- Update specified pod with the label 'unhealthy' and the value 'true':

`kubectl label pods {{name}} unhealthy=true`

- List all resources with different types:

`kubectl get all`

- Display resource (CPU/Memory/Storage) usage of nodes or pods:

`kubectl top pod`

- Print the address of the master and cluster services:

`kubectl cluster-info`

- Display an explanation of the specific field:

`kubectl explain pods.spec.containers`

- Print the logs for a container in a pod or specified resource:

`kubectl logs my-pod`

- Run command in an existing pod:

`kubectl exec my-pod -- ls /`
