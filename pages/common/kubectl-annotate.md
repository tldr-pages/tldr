# kubectl annotate

> Annotates Kubernetes resources.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#annotate>.

- Annotate a pod:

`kubectl annotate {{[po|pod]}} {{pod_name}} {{key}}={{value}}`

- Update a pod annotation by overwriting the existing value:

`kubectl annotate --overwrite pod {{pod_name}} {{key}}={{value}}`

- Annotate all pods in a namespace with a specific label selector:

`kubectl annotate {{[po|pods]}} -l {{label_key}}={{label_value}} {{key}}={{value}}`

- List all annotations a pod has:

`kubectl annotate {{[po|pod]}} {{pod_name}} --list`

- Remove the annotation from a pod:

`kubectl annotate {{[po|pod]}} {{pod_name}} {{key}}-`
