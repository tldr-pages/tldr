# kind

> Tool for running local Kubernetes clusters using Docker container "nodes".
> Designed for testing Kubernetes itself, but may be used for local development or continuous integration.
> More information: <https://github.com/kubernetes-sigs/kind>.

- Create a local Kubernetes cluster:

`kind create cluster --name {{cluster-name}}`

- Delete one or more clusters:

`kind delete clusters {{cluster-name}}`

- Get one of [clusters, nodes, kubeconfig]:

`kind get clusters`

- Export one of [kubeconfig, logs]:

`kind export logs`
