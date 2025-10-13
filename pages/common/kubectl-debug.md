# kubectl debug

> Debug cluster resources using interactive debugging containers.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_debug>.

- Create an interactive debugging session in a pod and immediately attach to it:

`kubectl debug {{pod_name}} {{[-it|--stdin --tty]}} --image busybox`

- Create a debug container with a custom image and name:

`kubectl debug --image {{image}} {{[-c|--container]}} {{container_name}} {{pod_name}}`

- Create an interactive debugging session on a node and immediately attach to it (the container will run in the host namespaces and the host's filesystem will be mounted at `/host`):

`kubectl debug node/{{node_name}} {{[-it|--stdin --tty]}} --image busybox`

- Create a copy of a pod and add a debug container to it:

`kubectl debug {{pod_name}} {{[-it|--stdin --tty]}} --image {{image}} --copy-to {{pod_copy_name}}`

- Create a copy of a pod and change the command of a specific container:

`kubectl debug {{pod_name}} {{[-it|--stdin --tty]}} --copy-to {{pod_copy_name}} --container {{container_name}} -- {{command}}`

- Create a copy of a pod and change the image of a specific container:

`kubectl debug {{pod_name}} --copy-to {{pod_copy_name}} --set-image {{container_name}}={{image}}`

- Create a copy of a pod and change all container images:

`kubectl debug {{pod_name}} --copy-to {{pod_copy_name}} --set-image '*={{image}}'`

- Create an ephemeral debug container and target a specific container (useful for debugging distroless containers):

`kubectl debug {{pod_name}} {{[-it|--stdin --tty]}} --image {{image}} --target {{target_container_name}}`
