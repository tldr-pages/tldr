# puppet apply

> Apply Puppet manifests locally.
> More information: <https://github.com/puppetlabs/puppet/blob/main/references/man/apply.md>.

- Apply a manifest:

`puppet apply {{path/to/manifest}}`

- Execute puppet code:

`puppet apply --execute {{code}}`

- Use a specific module and hiera configuration file:

`puppet apply --modulepath {{path/to/directory}} --hiera_config {{path/to/file}} {{path/to/manifest}}`
