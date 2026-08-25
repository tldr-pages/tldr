# flux

> Continuous and progressive delivery solution for Kubernetes.
> More information: <https://fluxcd.io/flux/cmd/>.

- Check if the Flux prerequisites are met on the cluster:

`flux check --pre`

- Bootstrap Flux on a Kubernetes cluster:

`flux bootstrap {{github|gitlab}} --owner {{owner}} --repository {{repository}} --path {{path/to/cluster_directory}}`

- Create a new GitRepository source:

`flux create source git {{source_name}} --url {{https://github.com/repository}} --branch {{branch_name}}`

- List all Flux custom resources:

`flux get all`

- Trigger a reconciliation for a specific Kustomization and apply changes from source:

`flux reconcile kustomization {{name}} --with-source`

- Suspend reconciliation for a Kustomization:

`flux suspend kustomization {{name}}`

- Resume reconciliation for a Kustomization:

`flux resume kustomization {{name}}`

- Display help for a specific subcommand:

`flux {{subcommand}} --help`
