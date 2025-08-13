# kubectl exec

> Execute a command in a container.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#exec>.

- Open bash in a pod:

`kubectl exec {{pod_name}} {{-it|--stdin --tty]}} -- bash`

