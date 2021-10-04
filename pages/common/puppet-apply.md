# puppet apply

> Apply Puppet manifests locally.
> More information: <https://puppet.com/docs/puppet/7/man/apply.html>.

- Apply a manifest:

`puppet apply {{path/to/manifest}}`

- Execute puppet code from the commandline:

`puppet apply --execute {{code}}`

- Use a specific module and hiera directory:

`puppet apply --modulepath {{path/to/directory}} --hiera_data {{path/to/directory}} {{path/to/manifest}}`
