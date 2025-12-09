# kubectl apply

> Manage applications through files defining Kubernetes resources.
> Create and update resources in a cluster.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_apply>.

- Apply a configuration to a resource by file name:

`kubectl apply {{[-f|--filename]}} {{path/to/file}}`

- Apply a configuration to a resource from `kustomization.yaml` in a directory:

`kubectl apply {{[-k|--kustomize]}} {{path/to/directory}}`

- Apply a configuration to a resource by `stdin`:

`{{cat pod.json}} | kubectl apply {{[-f|--filename]}} -`

- Edit the latest last-applied-configuration annotations of resources from the default editor:

`kubectl apply edit-last-applied {{[-f|--filename]}} {{path/to/file}}`

- Set the latest last-applied-configuration annotations by setting it to match the contents of a file:

`kubectl apply set-last-applied {{[-f|--filename]}} {{path/to/file}}`

- View the latest last-applied-configuration annotations by type/name or file:

`kubectl apply view-last-applied {{[-f|--filename]}} {{path/to/file}}`
