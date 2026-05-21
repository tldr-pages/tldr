# flux create

> Create or update Flux resources.
> More information: <https://fluxcd.io/flux/cmd/flux_create/>.

- Create a GitRepository source:

`flux create source git {{source_name}} --url {{https://github.com/repository}} --branch {{branch_name}}`

- Create a Kustomization resource to sync a directory from a Git source:

`flux create kustomization {{kustomization_name}} --source {{source_name}} --path {{path/to/directory}}`

- Create a HelmRelease:

`flux create helmrelease {{release_name}} --chart {{chart_name}} --source {{HelmRepository/repository_name}}`

- Create a Secret to authenticate with a Git repository:

`flux create secret git {{secret_name}} --url {{https://github.com/repository}} --username "{{username}}" --password "{{password}}"`
