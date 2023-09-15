# linode-cli lke

> Manage Linode Kubernetes Engine (LKE) clusters.
> See also: `linode-cli`.
> More information: <https://www.linode.com/docs/products/tools/cli/guides/linode-kubernetes-engine/>.

- List all LKE clusters:

`linode-cli lke clusters list`

- Create a new LKE cluster:

`linode-cli lke clusters create --region {{region}} --type {{type}} --node-type {{node_type}} --nodes-count {{count}}`

- View details of a specific LKE cluster:

`linode-cli lke clusters view {{cluster_id}}`

- Update an existing LKE cluster:

`linode-cli lke clusters update {{cluster_id}} --node-type {{new_node_type}}`

- Delete an LKE cluster:

`linode-cli lke clusters delete {{cluster_id}}`
