# kubectl top

> See the resource consumption for nodes or pods.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_top>.

- Get the resource consumption of all nodes:

`kubectl top {{node|nodes}}`

- Get resource consumption of a specific node:

`kubectl top {{node|nodes}} {{node_name}}`

- Get resource consumption of all pods:

`kubectl top {{po|pod|pods}}`

- Get resource consumption of a specific pod:

`kubectl top {{po|pod|pods}} {{pod_name}}`

- Get resource consumption of all pods in a namespace:

`kubectl top {{po|pod|pods}} --namespace {{namespace_name}}`

- Get resource consumption of all containers in a pod:

`kubectl top {{po|pod|pods}} --containers`

- Get resource consumption of all pods with specified label:

`kubectl top {{po|pod|pods}} -l {{key=value}}`
