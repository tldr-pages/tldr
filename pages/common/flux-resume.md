# flux resume

> Resume suspended Flux resources.
> More information: <https://fluxcd.io/flux/cmd/flux_resume/>.

- Resume reconciliation for a Kustomization:

`flux resume kustomization {{kustomization_name}}`

- Resume reconciliation for all Kustomizations in a namespace:

`flux resume kustomization --all`

- Resume reconciliation for a HelmRelease:

`flux resume helmrelease {{release_name}}`

- Resume reconciliation for a GitRepository source:

`flux resume source git {{source_name}}`

- Resume reconciliation for an ImageUpdateAutomation resource:

`flux resume image update {{automation_name}}`
