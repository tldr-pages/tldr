# flux delete

> Delete sources and resources in Flux.
> More information: <https://fluxcd.io/flux/cmd/flux_delete/>.

- Delete a Kustomization:

`flux delete kustomization {{kustomization_name}}`

- Delete a Kustomization without asking for confirmation:

`flux delete kustomization {{kustomization_name}} {{[-s|--silent]}}`

- Delete a HelmRelease:

`flux delete helmrelease {{release_name}}`

- Delete a GitRepository source:

`flux delete source git {{source_name}}`

- Delete a HelmRepository source:

`flux delete source helm {{source_name}}`
