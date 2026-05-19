# flux create

> Create or update Flux resources.
> More information: <https://fluxcd.io/flux/cmd/flux_create/>.

- Create a GitRepository source:

`flux create source git {{name}} --url={{https://github.com/repository}} --branch={{main}}`

- Create a Kustomization resource to sync a directory from a Git source:

`flux create kustomization {{name}} --source={{GitRepository/name}} --path={{./path}}`

- Create a HelmRelease:

`flux create helmrelease {{name}} --chart={{chart_name}} --source={{HelmRepository/repository_name}}`

- Create a Secret to authenticate with a Git repository:

`flux create secret git {{name}} --url={{https://github.com/repository}} --username={{username}} --password={{password}}`
