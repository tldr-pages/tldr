# kubectl attach

> Attach to a process that is already running inside an existing container.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_attach/>.

- Get output from a pod:

`kubectl attach {{pod_name}}`

- Get output from a container in the specified pod:

`kubectl attach {{pod_name}} {{[-c|--container]}} {{container_name}}`

- Get output from the first pod of a replica set:

`kubectl attach {{[rs|replicaset]}}/{{replicaset_name}}`

- Create an interactive session with a pod:

`kubectl attach {{pod_name}} {{[-it|--stdin --tty]}}`

- Create an interactive session with a specific container from a pod:

`kubectl attach {{pod_name}} {{[-c|--container]}} {{container_name}} {{[-it|--stdin --tty]}}`
