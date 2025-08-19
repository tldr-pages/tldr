# lxc-create

> Create linux containers.
> More information: <https://linuxcontainers.org/lxc/getting-started/>.

- Create a container interactively in `/var/lib/lxc/`:

`sudo lxc-create {{[-n|--name]}} {{container_name}} {{[-t|--template]}} download`

- Create a container in a target directory:

`sudo lxc-create {{[-P|--lxcpath]}} /{{path/to/directory}}/ {{[-n|--name]}} {{container_name}} {{[-t|--template]}} download`

- Create a container passing options to a template:

`sudo lxc-create {{[-n|--name]}} {{container_name}} {{[-t|--template]}} download -- {{[-d|--dist]}} {{distro-name}} {{[-r|--release]}} {{release-version}} {{[-a|--arch]}} {{arch}}`

- Display help:

`lxc-create {{[-?|--help]}}`
