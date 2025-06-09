# k3s

> Install and manage lightweight Kubernetes clusters using the k3s CLI.
> More information: <https://docs.k3s.io/cli/k3s>.

- Install a single-node K3s server with default settings:

`curl {{[-sfL|--silent --fail --location]}} https://get.k3s.io | sh -s - server`

- Install a K3s server without deploying a local agent:

`curl {{[-sfL|--silent --fail --location]}} https://get.k3s.io | sh -s - server --disable {{agent}}`

- Install a K3s agent that connects to a server:

`curl {{[-sfL|--silent --fail --location]}} https://get.k3s.io | sh -s - agent {{[-s|--server]}} {{https://myserver:6443}} {{[-t|--token]}} {{mytoken}}`

- Run the embedded `kubectl` command:

`k3s kubectl get nodes`

- Take an etcd snapshot of the cluster:

`k3s etcd-snapshot save`

- Rotate the CA certificate:

`k3s certificate rotate-ca`

- Manage bootstrap tokens:

`k3s token list`

- Uninstall K3s and remove all components:

`k3s-uninstall.sh`
