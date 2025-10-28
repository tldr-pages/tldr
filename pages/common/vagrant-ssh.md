# vagrant ssh

> SSH into a running Vagrant machine.
> See also: `vagrant`.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/ssh>.

- SSH into the machine running in the current directory:

`vagrant ssh`

- Target a running machine by name or ID:

`vagrant ssh {{name|id}}`

- Execute an SSH command and exit:

`vagrant ssh {{[-c|--command]}} {{ssh_command}}`

- SSH without authentication, leaving authentication up to the user:

`vagrant ssh {{[-p|--plain]}}`
