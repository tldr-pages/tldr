# kubectl apply

> Manage applications through files defining Kubernetes resources.
> Create and update resources in a cluster.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply>.

- Apply a configuration to a resource by file name or `stdin`:

`kubectl apply -f {{resource_filename}}`

- Edit the latest last-applied-configuration annotations of resources from the default editor:

`kubectl apply edit-last-applied -f {{resource_filename}}`

- Set the latest last-applied-configuration annotations by setting it to match the contents of a file:

`kubectl apply set-last-applied -f {{resource_filename}}`

- View the latest last-applied-configuration annotations by type/name or file:

`kubectl apply view-last-applied -f {{resource_filename}}`
