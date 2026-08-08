# kubectl krew

> Plugin manager for `kubectl`.
> More information: <https://krew.sigs.k8s.io/docs/>.

- Search for available plugins:

`kubectl krew search`

- Install a plugin:

`kubectl krew install {{plugin_name}}`

- List installed plugins:

`kubectl krew list`

- Update the local plugin index:

`kubectl krew update`

- Upgrade all installed plugins:

`kubectl krew upgrade`

- Get information about a plugin:

`kubectl krew info {{plugin_name}}`

- Uninstall a plugin:

`kubectl krew uninstall {{plugin_name}}`

> See also: `kubectl-plugin`.