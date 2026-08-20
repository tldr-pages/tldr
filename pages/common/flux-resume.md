# flux resume

> Resume the reconciliation of suspended Flux resources.
> See also: `flux suspend`.
> More information: <https://fluxcd.io/flux/cmd/flux_resume/>.

- Resume a Kustomization:

`flux resume kustomization {{name}}`

- Resume a HelmRelease:

`flux resume helmrelease {{name}}`

- Resume a source of a specific kind:

`flux resume source {{git|helm|bucket|oci|chart}} {{name}}`

- Resume all Kustomizations in the current namespace:

`flux resume kustomization --all`

- Resume all Kustomizations, waiting for each one to reconcile before moving on to the next:

`flux resume kustomization --all --wait`

- Resume a resource in a specific namespace:

`flux resume kustomization {{name}} --namespace {{namespace}}`
