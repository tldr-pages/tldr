# flux get

> Display the status of Flux resources.
> More information: <https://fluxcd.io/flux/cmd/flux_get/>.

- List all resources and statuses across all namespaces:

`flux get all {{[-A|--all-namespaces]}}`

- List all Kustomizations and their statuses:

`flux get kustomizations`

- List all Kustomizations with source information:

`flux get kustomizations --show-source`

- List all HelmReleases:

`flux get helmreleases`

- List all GitRepository sources:

`flux get sources git`

- Watch Kustomizations for changes:

`flux get kustomizations {{[-w|--watch]}}`
