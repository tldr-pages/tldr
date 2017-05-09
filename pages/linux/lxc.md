# lxc

> Manage Linux containers (using the lxd REST API).

- List all containers (does not work on public remotes):

`lxc list [{{private-remote}}:][{{filter}}]`

- List all images:

`lxc image list [{{remote}}:][{{filter}}]`

- Create a new container from an image (i.e. `ubuntu:16.04`):

`lxc launch [{{remote}}:]{{image}} {{container-name}}`

- Start a container:

`lxc start [{{remote}}:]{{container-name}}`

- Stop a container:

`lxc stop [{{remote}}:]{{container-name}}`

- Show detailed info about a container:

`lxc info [{{remote}}:]{{container-name}}`

- Take a snapshot of a container:

`lxc snapshot [{{remote}}:]{{container-name}} {{snapshot-name}}`
