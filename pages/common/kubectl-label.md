# kubectl label

> Label Kubernetes resources.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_label>.

- Label a pod:

`kubectl label {{[po|pods]}} {{pod_name}} {{key}}={{value}}`

- Update a pod label by overwriting the existing value:

`kubectl label {{[po|pods]}} {{pod_name}} {{key}}={{value}} --overwrite`

- Label all pods in the namespace:

`kubectl label {{[po|pods]}} {{key}}={{value}} --all`

- Label a pod identified by the pod definition file:

`kubectl label {{[-f|--filename]}} {{pod_definition_file}} {{key}}={{value}}`

- Remove the label from a pod:

`kubectl label {{[po|pods]}} {{pod_name}} {{key}}-`
