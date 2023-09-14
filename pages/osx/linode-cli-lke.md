# linode-cli lke

> Command-line interface to manage Linode Kubernetes Engine (LKE) clusters via `linode-cli`.

- List all LKE clusters:

`linode-cli lke clusters list`

- Create a new LKE cluster:

`linode-cli lke clusters create --region [region] --type [type] --node-type [node-type] --nodes-count [count]`

- View details of a specific LKE cluster:

`linode-cli lke clusters view [cluster-id]`

- Update an existing LKE cluster:

`linode-cli lke clusters update [cluster-id] --node-type [new-node-type]`

- Delete an LKE cluster:

`linode-cli lke clusters delete [cluster-id]`
