# pct create

> Create LXC containers in Proxmox.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_create>.

- Create a container from a template with 4GB size, give it 512MiB of memory and unlimited access to CPU:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:4`

- Create a container from a template and give it a specific memory limit in megabytes:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:{{4}} --memory {{8192}}`

- Create a container from a template and give it a hostname and a password:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:{{4}} --hostname {{hostname}} --password {{password}}`

- Create a container from a template and give it network access:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:{{4}} --net0 name={{eth0}},bridge={{vmbr0}},ip={{dhcp|manual|10.0.0.1/24}} --features nesting=1`

- Start a container immediately after creation:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:{{4}} --start`
