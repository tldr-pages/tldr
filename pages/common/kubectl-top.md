# kubectl top

> See the resource consumption for nodes or pods.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_top>.

- Get the resource consumption of all nodes:

`kubectl top {{[no|nodes]}}`

- Get resource consumption of a specific node:

`kubectl top {{[no|nodes]}} {{node_name}}`

- Get resource consumption of all pods:

`kubectl top {{[po|pods]}}`

- Get resource consumption of a specific pod:

`kubectl top {{[po|pods]}} {{pod_name}}`

- Get resource consumption of all pods in a namespace:

`kubectl top {{[po|pods]}} {{[-n|--namespace]}} {{namespace_name}}`

- Get resource consumption of all containers in a pod:

`kubectl top {{[po|pods]}} --containers`

- Get resource consumption of all pods with the specified label:

`kubectl top {{[po|pods]}} {{[-l|--selector]}} {{key=value}}`
