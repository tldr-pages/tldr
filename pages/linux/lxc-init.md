# lxc init

> Create LXD instances from images without starting them.
> More information: <https://canonical.com/lxd/docs/latest/reference/manpages/lxc/init/>.

- Create a container from an image without starting it:

`sudo lxc init {{ubuntu:24.04}} {{instance_name}}`

- Create a container with configuration from a YAML file:

`sudo lxc init {{ubuntu:24.04}} {{instance_name}} < {{path/to/config.yaml}}`

- Create a virtual machine:

`sudo lxc init {{ubuntu:24.04}} {{instance_name}} --vm`

- Create a virtual machine with a number of vCPUs and an amount of memory:

`sudo lxc init {{ubuntu:24.04}} {{instance_name}} --vm {{[-c|--config]}} limits.cpu={{4}} {{[-c|--config]}} limits.memory={{4GiB}}`
