# microk8s

> Lightweight Kubernetes distribution packaged as a snap.
> More information: <https://microk8s.io/docs>.

- Show the status of the cluster:

`microk8s status`

- Start the cluster:

`microk8s start`

- Stop the cluster:

`microk8s stop`

- Enable an addon such as `dns` or `ingress`:

`microk8s enable {{addon}}`

- Disable an addon:

`microk8s disable {{addon}}`

- Run `kubectl` against the cluster:

`microk8s kubectl {{get pods --all-namespaces}}`

- Print the kubeconfig:

`microk8s config`

- Join a node to the cluster:

`microk8s join {{node_ip}}:{{port}}/{{token}}`
