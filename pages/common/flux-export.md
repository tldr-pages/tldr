# flux export

> Export Flux resources in YAML format.
> More information: <https://fluxcd.io/flux/cmd/flux_export/>.

- Export a Kustomization:

`flux export kustomization {{name}}`

- Export a source of a specific kind:

`flux export source {{git|helm|bucket|oci}} {{name}}`

- Export all Kustomizations in the current namespace:

`flux export kustomization --all`

- Export all sources of a specific kind to a file:

`flux export source git --all > {{path/to/sources.yaml}}`

- Export a HelmRelease from a specific namespace:

`flux export helmrelease {{name}} --namespace {{namespace}}`
