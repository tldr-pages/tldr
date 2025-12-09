# puppet

> Manage and automate the configuration of servers.
> Puppet uses a declarative language to define system configurations and apply them automatically.
> Some subcommands, such as `agent` and `apply`, have their own usage documentation.
> More information: <https://github.com/puppetlabs/puppet/blob/main/references/man/overview.md>.

- Apply a Puppet manifest file to configure the system:

`puppet apply {{path/to/file.pp}}`

- Apply a manifest in no operation (dry-run) mode to preview changes:

`puppet apply --noop {{path/to/file.pp}}`

- Validate the syntax of a Puppet manifest:

`puppet parser validate {{path/to/file.pp}}`

- Run the Puppet agent to fetch and apply configurations from the master:

`puppet agent {{[-t|--test]}}`

- Display help for a specific subcommand:

`puppet help {{subcommand}}`

- Display general help:

`puppet {{[-h|--help]}}`

- Display version:

`puppet {{[-V|--version]}}`
