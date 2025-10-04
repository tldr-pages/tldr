# Talosctl

> Talosctl is a cli for interacting with Talos Linux, a minimal and immutable Kubernetes distribution.
> See also: `kubectl`.
> More information: <https://www.talos.dev/v1.9/reference/cli/>.

- Apply a config to a fresh node:

`talosctl apply-config --insecure --nodes {{control_plane_ip}} --file {{controlplane.yaml}}`

- Bootstrap the etcd cluster on a node:

`talosctl bootstrap --nodes {{node_ip}} --talosconfig={{./talosconfig}}`

- Edit an API resource:

`talosctl edit {{resource_to_edit}} --nodes {{node_ip}} --talosconfig={{./talosconfig}}`

- Get resources:

`talosctl get {{resource_to_get}} --nodes {{node_ip}} --talosconfig={{./talosconfig}}`

- Download the admin kube config from a node:

`talosctl kubeconfig --nodes {{node_ip}} --talosconfig={{./talosconfig}}`

- Reset a node:

`talosctl reset --nodes {{node_ip}} --talosconfig={{./talosconfig}}`
