# k3d

> Create and manage lightweight k3s Kubernetes clusters inside Docker.
> More information: <https://k3d.io/stable/usage/commands/>.

- Create a cluster:

`k3d cluster create {{cluster_name}}`

- Create a cluster with multiple server and agent nodes:

`k3d cluster create {{cluster_name}} {{[-s|--servers]}} {{1}} {{[-a|--agents]}} {{2}}`

- List existing clusters:

`k3d cluster list`

- List clusters as JSON (or YAML):

`k3d cluster list {{[-o|--output]}} {{json|yaml}}`

- List clusters without table headers (useful for scripting):

`k3d cluster list --no-headers`

- Stop or start a cluster:

`k3d cluster {{stop|start}} {{cluster_name}}`

- Delete a cluster:

`k3d cluster delete {{cluster_name}}`

- Print the kubeconfig for a cluster:

`k3d kubeconfig get {{cluster_name}}`
