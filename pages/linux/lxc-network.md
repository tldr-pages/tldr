# lxc network

> Manage networks for LXD containers.
> More information: <https://linuxcontainers.org/lxd/docs/master/networks>.

- List all available networks:

`lxc network list`

- Show the configuration of a specific network:

`lxc network show {{network_name}}`

- Add a running instance to a specific network:

`lxc network attach {{network_name}} {{container_name}}`

- Create a new managed network:

`lxc network create {{network_name}}`

- Set a bridge interface of a specific network:

`lxc network set {{network_name}} bridge.external_interfaces {{eth0}}`

- Disable NAT for a specific network:

`lxc network set {{network_name}} ipv{{4}}.nat false`
