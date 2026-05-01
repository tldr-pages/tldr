# flux

> Continuous and progressive delivery solution for Kubernetes.
> More information: <https://fluxcd.io/flux/cmd/>.

- Check if the Flux prerequisites are met on the cluster:

`flux check --pre`

- Bootstrap Flux on a Kubernetes cluster:

`flux bootstrap {{github|gitlab}} --owner={{owner}} --repository={{repository}} --path={{clusters/my-cluster}}`

- List all Flux custom resources:

`flux get all`

- Trigger a reconciliation for a specific Kustomization:

`flux reconcile kustomization {{name}}`

- Suspend reconciliation for a Kustomization:

`flux suspend kustomization {{name}}`

- Display help for a specific subcommand:

`flux {{subcommand}} --help`

