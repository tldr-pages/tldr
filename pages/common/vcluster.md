# vcluster

> Create and manage lightweight virtual Kubernetes clusters in namespaces.
> More information: <https://www.vcluster.com/docs/vcluster>.

- Create a virtual cluster in a specific namespace:

`vcluster create {{vcluster_name}} {{[-n|--namespace]}} {{namespace}}`

- Connect to a virtual cluster with a local port and insecure mode:

`vcluster connect {{vcluster_name}} {{[-n|--namespace]}} {{namespace}} --local-port {{port}} --insecure`

- List all virtual clusters:

`vcluster list`

- Delete a virtual cluster:

`vcluster delete {{vcluster_name}}`

- List platform-managed virtual clusters:

`vcluster platform list`

- Create a platform-managed virtual cluster:

`vcluster platform create {{vcluster_name}} {{[-n|--namespace]}} {{namespace}}`

- Connect to a platform-managed virtual cluster:

`vcluster platform connect {{vcluster_name}} {{[-n|--namespace]}} {{namespace}}`

- Delete a platform-managed virtual cluster:

`vcluster platform delete {{vcluster_name}} {{[-n|--namespace]}} {{namespace}}`
