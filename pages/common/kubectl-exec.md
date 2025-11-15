# kubectl exec

> Execute a command in a container.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_exec>.

- Open Bash in a pod, using the first container by default:

`kubectl exec {{pod_name}} {{[-it|--stdin --tty]}} -- bash`
