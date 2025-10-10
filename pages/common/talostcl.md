# talosctl

> Interact with Talos Linux, a minimal and immutable Kubernetes distribution.
> See also: `kubectl`.
> More information: <https://www.talos.dev/latest/reference/cli/>.

- Apply a config to a fresh node:

`talosctl apply-config {{[-i|--insecture]}} {{[-n|--nodes]}} {{control_plane_ip}} {{[-f|--file]}} {{path/to/control_plane.yaml}}`

- Bootstrap the `etcd` cluster on a node:

`talosctl bootstrap {{[-n|--nodes]}} {{node_ip}}`

- Edit an API resource:

`talosctl edit {{resource_to_edit}} {{[-n|--nodes]}} {{node_ip}}`

- Get resources:

`talosctl get {{resource_to_get}} {{[-n|--nodes]}} {{node_ip}}`

- Download the admin kube configuration from a node:

`talosctl kubeconfig {{[-n|--nodes]}} {{node_ip}}`

- Reset a node:

`talosctl reset {{[-n|--nodes]}} {{node_ip}}`
