# flux reconcile

> Trigger a reconciliation of Flux sources and resources.
> More information: <https://fluxcd.io/flux/cmd/flux_reconcile/>.

- Reconcile a Kustomization:

`flux reconcile kustomization {{name}}`

- Reconcile a Kustomization together with its source:

`flux reconcile kustomization {{name}} --with-source`

- Reconcile a source of a specific kind:

`flux reconcile source {{git|helm|bucket|oci|chart}} {{name}}`

- Reconcile a HelmRelease:

`flux reconcile helmrelease {{name}}`

- Reconcile a HelmRelease and its source:

`flux reconcile helmrelease {{name}} --with-source`

- Reconcile an image repository to scan for new tags:

`flux reconcile image repository {{name}}`

- Reconcile a resource in a specific namespace:

`flux reconcile kustomization {{name}} --namespace {{namespace}}`
