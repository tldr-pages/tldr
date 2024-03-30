# linode-cli lke

> Beheer Linode Kubernetes Engine (LKE) clusters.
> Bekijk ook: `linode-cli`.
> Meer informatie: <https://www.linode.com/docs/products/tools/cli/guides/linode-kubernetes-engine/>.

- Toon alle LKE clusters:

`linode-cli lke clusters list`

- Maak een nieuw LKE cluster:

`linode-cli lke clusters create --region {{region}} --type {{type}} --node-type {{node_type}} --nodes-count {{count}}`

- Toon details van een specifiek LKE cluster:

`linode-cli lke clusters view {{cluster_id}}`

- Update een bestaand LKE cluster:

`linode-cli lke clusters update {{cluster_id}} --node-type {{new_node_type}}`

- Verwijder een LKE cluster:

`linode-cli lke clusters delete {{cluster_id}}`
