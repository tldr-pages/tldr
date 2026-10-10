# flux reconcile

> Trigger a reconciliation of Flux sources and resources.
> More information: <https://fluxcd.io/flux/cmd/flux_reconcile/>.

- Trigger reconciliation of a GitRepository source:

`flux reconcile source git {{source_name}}`

- Trigger reconciliation of a Kustomization:

`flux reconcile kustomization {{kustomization_name}}`

- Trigger reconciliation of a Kustomization and its source:

`flux reconcile kustomization {{kustomization_name}} --with-source`

- Trigger reconciliation of a HelmRelease:

`flux reconcile helmrelease {{release_name}}`

- Trigger reconciliation of a HelmRelease and its source:

`flux reconcile helmrelease {{release_name}} --with-source`
