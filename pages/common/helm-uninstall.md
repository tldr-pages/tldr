# helm uninstall

> Uninstall one or more helm releases.
> More information: <https://helm.sh/docs/helm/helm_uninstall/>.

- Uninstall a release:

`helm uninstall {{release_name}}`

- Uninstall multiple releases:

`helm uninstall {{release_name1}} {{release_name2}}`

- Uninstall a release in a specific namespace:

`helm uninstall {{release_name}} {{[-n|--namespace]}} {{namespace}}`

- Uninstall a release but keep its history:

`helm uninstall {{release_name}} --keep-history`

- Simulate an uninstall without actually doing it:

`helm uninstall {{release_name}} --dry-run`

- Uninstall a release and wait until its resources are deleted:

`helm uninstall {{release_name}} --wait`

- Uninstall a release without running hooks:

`helm uninstall {{release_name}} --no-hooks`
