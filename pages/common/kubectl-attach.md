# kubectl attach

> Attach to a running container in a pod.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_attach>.

- Attach to the first container in a pod:

`kubectl attach {{pod_name}}`

- Attach to a specific container in a pod:

`kubectl attach {{[-c|--container]}} {{container_name}} {{pod_name}}`

- Attach to a pod with stdin:

`kubectl attach {{[-i|--stdin]}} {{pod_name}}`

- Attach to a pod with stdin and a TTY (for interactive processes):

`kubectl attach {{[-it|--stdin --tty]}} {{pod_name}}`

- Attach to a pod without stdin, only showing output:

`kubectl attach --stdin={{false}} {{pod_name}}`

- Attach to the first container matching a label selector:

`kubectl attach {{[-l|--selector]}} {{label_key}}={{label_value}}`
