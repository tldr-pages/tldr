# vagrant port

> List mappings between guest and host ports.
> See also: `vagrant`.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/port>.

- List all port mappings:

`vagrant port`

- List mappings for a specific machine (if `Vagrantfile` is multi-machine):

`vagrant port {{machine_name}}`

- Display info for a specific guest port:

`vagrant port --guest {{port_number}}`

- Display machine-readable output:

`vagrant port --machine-readable`
