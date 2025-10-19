# vagrant provision

> Run configured provisioners on a running Vagrant machine.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/provision>.

- Run all provisioners for the default machine:

`vagrant provision`

- Run provisioners for a specific machine:

`vagrant provision {{machine_name}}`

- Run only the specified provisioners (comma-separated):

`vagrant provision --provision-with {{shell}}`

- Run a subset of provisioners in order:

`vagrant provision --provision-with {{shell,ansible_local}}`
