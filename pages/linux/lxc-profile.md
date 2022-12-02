# lxc profile

> Manage profiles for LXD containers.
> More information: <https://linuxcontainers.org/lxd/docs/master/profiles>.

- List all available profiles:

`lxc profile list`

- Show the configuration of a specific profile:

`lxc profile show {{path/to/file}}`

- Edit a specific profile in the default editor:

`lxc profile edit {{path/to/file}}`

- Edit a specific profile importing the configuration values from a file:

`lxc profile edit {{path/to/file}} < {{config.yaml}}`

- Launch a new container with specific profiles:

`lxc launch {{container_image}} {{container_name}} --profile {{path/to/file}} --profile {{path/to/file}}`

- Change the profiles of a running container:

`lxc profile assign {{container_name}} {{path/to/file}}`
