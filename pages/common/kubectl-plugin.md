# kubectl plugin

> Manage kubectl plugins that extend the functionality of the command.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_plugin/>.

- List all available plugins on the system `$PATH`:

`kubectl plugin list`

- List only the executable names of available plugins without full paths:

`kubectl plugin list --name-only`

- Display help:

`kubectl plugin --help`
