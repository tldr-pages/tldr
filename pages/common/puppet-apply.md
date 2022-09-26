# puppet apply

> Apply Puppet manifests locally.
> More information: <https://puppet.com/docs/puppet/7/man/apply.html>.

- Apply a manifest:

`puppet apply {{path/to/manifest}}`

- Execute puppet code:

`puppet apply --execute {{code}}`

- Use a specific module and hiera config file:

`puppet apply --modulepath {{path/to/directory}} --hiera_config {{path/to/file}} {{path/to/manifest}}`
