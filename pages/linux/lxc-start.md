# lxc-start

> Start a container.
> More information: <https://linuxcontainers.org/lxc/getting-started/>.

- Start the lxc service:

`systemctl start lxc-net`

- Start a container:

`sudo lxc-start {{container_name}}`

- Start a container in the foreground:

`sudo lxc-start {{[-F|--foreground]]}`
