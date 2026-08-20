# flux suspend

> Suspend the reconciliation of Flux resources.
> See also: `flux resume`.
> More information: <https://fluxcd.io/flux/cmd/flux_suspend/>.

- Suspend a Kustomization:

`flux suspend kustomization {{name}}`

- Suspend a HelmRelease:

`flux suspend helmrelease {{name}}`

- Suspend a source of a specific kind:

`flux suspend source {{git|helm|bucket|oci|chart}} {{name}}`

- Suspend all Kustomizations in the current namespace:

`flux suspend kustomization --all`

- Suspend a resource in a specific namespace:

`flux suspend kustomization {{name}} --namespace {{namespace}}`
