# talosctl

> Interact with Talos Linux, a minimal and immutable Kubernetes distribution.
> See also: `kubectl`.
> More information: <https://www.talos.dev/v1.9/reference/cli/>.

- Apply a config to a fresh node:

`talosctl apply-config {{[-i|--insecture]}} {{[-n|--nodes]}} {{control_plane_ip}} {{[-f|--files]}} {{path/to/controlplane.yaml}}`

- Bootstrap the `etcd` cluster on a node:

`talosctl bootstrap {{[-n|--nodes]}} {{node_ip}} --talosconfig={{path/to/talosconfig}}`

- Edit an API resource:

`talosctl edit {{resource_to_edit}} {{[-n|--nodes]}} {{node_ip}} --talosconfig={{path/to/talosconfig}}`

- Get resources:

`talosctl get {{resource_to_get}} {{[-n|--nodes]}} {{node_ip}} --talosconfig={{path/to/talosconfig}}`

- Download the admin kube configuration from a node:

`talosctl kubeconfig {{[-n|--nodes]}} {{node_ip}} --talosconfig={{path/to/talosconfig}}`

- Reset a node:

`talosctl reset {{[-n|--nodes]}} {{node_ip}} --talosconfig={{path/to/talosconfig}}`
