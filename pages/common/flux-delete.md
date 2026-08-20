# flux delete

> Delete Flux sources and resources from a cluster.
> More information: <https://fluxcd.io/flux/cmd/flux_delete/>.

- Delete a Kustomization:

`flux delete kustomization {{name}}`

- Delete a source of a specific kind:

`flux delete source {{git|helm|bucket|oci}} {{name}}`

- Delete a HelmRelease:

`flux delete helmrelease {{name}}`

- Delete a resource in a specific namespace:

`flux delete kustomization {{name}} --namespace {{namespace}}`

- Delete a resource without asking for confirmation:

`flux delete kustomization {{name}} --silent`
