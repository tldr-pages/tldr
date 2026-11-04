# flux uninstall

> Uninstall Flux and its custom resource definitions.
> More information: <https://fluxcd.io/flux/cmd/flux_uninstall/>.

- Uninstall Flux components, custom resources, and namespace:

`flux uninstall`

- Uninstall Flux without asking for confirmation:

`flux uninstall {{[-s|--silent]}}`

- Uninstall Flux from a specific namespace:

`flux uninstall {{[-n|--namespace]}} {{namespace}}`

- Uninstall Flux but keep the namespace:

`flux uninstall --keep-namespace`

- Simulate uninstalling Flux:

`flux uninstall --dry-run`
