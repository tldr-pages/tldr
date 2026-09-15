# talosctl

> Manage Talos Linux nodes and clusters from the command-line.
> More information: <https://www.talos.dev/latest/reference/cli/>.

- Display the version of talosctl and the connected node:

`talosctl version`

- List all nodes in the cluster:

`talosctl get members`

- Display the health of a cluster:

`talosctl health`

- Display logs from a service on a node:

`talosctl logs {{service_name}}`

- Reboot a node:

`talosctl reboot`

- Reset a node to its initial state:

`talosctl reset`

- Display information about a node's network interfaces:

`talosctl get addresses`
