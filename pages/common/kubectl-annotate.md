# kubectl annotate

> Annotates Kubernetes resources.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_annotate>.

- Annotate a pod:

`kubectl annotate {{[po|pods]}} {{pod_name}} {{key}}={{value}}`

- Update a pod annotation by overwriting the existing value:

`kubectl annotate {{[po|pods]}} {{pod_name}} {{key}}={{value}} --overwrite`

- Annotate all pods in a namespace with a specific label selector:

`kubectl annotate {{[po|pods]}} {{key}}={{value}} {{[-l|--selector]}} {{label_key}}={{label_value}}`

- List all annotations a pod has:

`kubectl annotate {{[po|pods]}} {{pod_name}} --list`

- Remove the annotation from a pod:

`kubectl annotate {{[po|pods]}} {{pod_name}} {{key}}-`
