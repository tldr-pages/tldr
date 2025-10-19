# vagrant up

> Create, configure, and provision Vagrant machines.
> More information: <https://developer.hashicorp.com/vagrant/docs/cli/up>.

- Boot and provision all machines defined in the Vagrantfile:

`vagrant up`

- Boot a specific machine by name:

`vagrant up {{machine_name}}`

- Boot using a specific provider:

`vagrant up --provider {{virtualbox}}`

- Force all provisioners to run on boot:

`vagrant up --provision`

- Run only selected provisioners during boot:

`vagrant up --provision-with {{shell}}`

- Disable parallel boot for multi-machine environments:

`vagrant up --no-parallel`

- Destroy a machine automatically if an error occurs during the initial boot:

`vagrant up --destroy-on-error`
