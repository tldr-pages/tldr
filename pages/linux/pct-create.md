# pct create

> Create LXC containers in Proxmox.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html>.

- Create a container from a template with 4GB size:

`pct {{[cr|create]}} {{100}} {{/var/lib/vz/template/cache/distro-name.tar.zst}} --rootfs {{local-lvm}}:4`

- Create a container from a template and give it a hostname and a password:

`pct {{[cr|create]}} {{100}} {{/var/lib/vz/template/cache/distro-name.tar.zst}} --rootfs {{local-lvm}}:{{4}} --hostname {{hostname}} --password {{password}}`

- Start a container immediately after creation:

`pct {{[cr|create]}} {{100}} {{/var/lib/vz/template/cache/distro-name.tar.zst}} --rootfs {{local-lvm}}:{{4}} --start`
