# flux get

> Get the statuses of Flux resources.
> More information: <https://fluxcd.io/flux/cmd/flux_get/>.

- List all Flux resources in the current namespace:

`flux get all`

- List all Flux resources across every namespace:

`flux get all --all-namespaces`

- List Kustomizations and their reconciliation status:

`flux get kustomizations`

- List sources of a specific kind:

`flux get sources {{git|helm|bucket|oci|chart}}`

- List HelmReleases in a specific namespace:

`flux get helmreleases --namespace {{namespace}}`

- List only the resources that are not ready:

`flux get all --status-selector {{ready=false}}`

- Filter resources by label:

`flux get kustomizations --label-selector {{key=value}}`

- Watch resources for status changes:

`flux get kustomizations --watch`
