# k3s

> Install and manage lightweight Kubernetes clusters.
> More information: <https://docs.k3s.io/cli>.

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
