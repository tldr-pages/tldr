# vagrant

> Manage lightweight, reproducible, and portable development environments.
> More information: <https://www.vagrantup.com>.

- Create Vagrantfile in current directory with the base Vagrant box:

`vagrant init`

- Create Vagrantfile with the Ubuntu 14.04 (Trusty Tahr) box from HashiCorp Atlas:

`vagrant init ubuntu/trusty32`

- Start and provision the vagrant environment:

`vagrant up`

- Suspend the machine:

`vagrant suspend`

- Halt the machine:

`vagrant halt`

- Connect to machine via SSH:

`vagrant ssh`

- Output the SSH configuration file of the running Vagrant machine:

`vagrant ssh-config`
