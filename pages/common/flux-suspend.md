# flux suspend

> Suspend Flux resources.
> More information: <https://fluxcd.io/flux/cmd/flux_suspend/>.

- Suspend reconciliation for a Kustomization:

`flux suspend kustomization {{kustomization_name}}`

- Suspend reconciliation for all Kustomizations in a namespace:

`flux suspend kustomization --all`

- Suspend reconciliation for a HelmRelease:

`flux suspend helmrelease {{release_name}}`

- Suspend reconciliation for a GitRepository source:

`flux suspend source git {{source_name}}`

- Suspend reconciliation for an ImageUpdateAutomation resource:

`flux suspend image update {{automation_name}}`
