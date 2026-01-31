# lxc-attach

> Attach to a container.
> More information: <https://linuxcontainers.org/lxc/getting-started/>.

- Attach to a container:

`sudo lxc-attach {{container_name}}`

- Attach to a container without passing host environment variables to it:

`sudo lxc-attach {{container_name}} --clear-env`

- Display help:

`lxc-attach {{[-?|--help]}}`
