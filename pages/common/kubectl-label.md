# kubectl label

> Label Kubernetes resources.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#label>.

- Label a pod:

`kubectl label pod {{pod_name}} {{key}}={{value}}`

- Update a pod label by overwriting the existing value:

`kubectl label --overwrite pod {{pod_name}} {{key}}={{value}}`

- Label all pods in the namespace:

`kubectl label pods --all {{key}}={{value}}`

- Label a pod identified by the pod definition file:

`kubectl label -f {{pod_definition_file}} {{key}}={{value}}`

- Remove the label from a pod:

`kubectl label pod {{pod_name}} {{key}}-`
