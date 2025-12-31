# vagrant

> Manage lightweight, reproducible, and portable development environments.
> Some subcommands such as `box`, `snapshot`, `halt`, etc. have their own usage documentation.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli>.

- Create a `Vagrantfile` in the current directory with the base Vagrant box:

`vagrant init`

- Create a `Vagrantfile` with a box from the Vagrant Public Registry:

`vagrant init {{ubuntu/focal64}}`

- Start and provision the Vagrant environment:

`vagrant up`

- Suspend the machine:

`vagrant suspend`

- Halt the machine:

`vagrant halt`

- Connect to the machine via SSH:

`vagrant ssh`

- Output the SSH configuration file of the running Vagrant machine:

`vagrant ssh-config`

- List all local boxes:

`vagrant box list`
