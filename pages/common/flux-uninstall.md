# flux uninstall

> Remove the Flux components and custom resources from a cluster.
> See also: `flux bootstrap`.
> More information: <https://fluxcd.io/flux/cmd/flux_uninstall/>.

- Display the objects that would be deleted, without removing them:

`flux uninstall --dry-run`

- Remove the Flux components and custom resources:

`flux uninstall`

- Remove Flux from a specific namespace:

`flux uninstall --namespace {{namespace}}`

- Remove the Flux components but keep the namespace:

`flux uninstall --keep-namespace`

- Remove Flux without asking for confirmation:

`flux uninstall --silent`
