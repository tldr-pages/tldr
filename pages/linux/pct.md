# pct

> Manage LXC containers in Proxmox.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html>.

- List all containers:

`pct list`

- Start/Stop/Reboot a specific container:

`pct {{start|stop|reboot}} {{100}}`

- Access a specific container's shell:

`pct {{[en|enter]}} {{100}}`

- Create a container from template with 4GB size:

`pct {{[cr|create]}} {{100}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:4`

- Resize the container's disk to 20G:

`pct {{[resi|resize]}} {{100}} {{rootfs|mpX}} {{20G}}`

- Show the configuration of a container, specifying its ID:

`pct {{[conf|config]}} {{100}}`

- Snapshot a specific container with description:

`pct {{[sn|snapshot]}} {{100}} {{my-snapshot}} --description {{My snapshot description}}`

- Destroy a container and remove all related resources:

`pct {{[des|destroy]}} {{100}} --purge`
