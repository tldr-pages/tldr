# flux export

> Export Flux resources in YAML format.
> More information: <https://fluxcd.io/flux/cmd/flux_export/>.

- Export a Kustomization:

`flux export kustomization {{kustomization_name}}`

- Export all Kustomization resources and save them to a file:

`flux export kustomization --all > {{path/to/kustomizations.yaml}}`

- Export a GitRepository source including credentials:

`flux export source git {{source_name}} --with-credentials`

- Export all GitRepository sources:

`flux export source git --all`

- Export a HelmRelease:

`flux export helmrelease {{release_name}}`
