# pct

> Manage LXC containers in Proxmox.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html>.

- List all containers:

`pct list`

- Start/Stop/Reboot a specific container:

`pct {{start|stop|reboot}} {{container_id}}`

- Access a specific container's shell:

`pct {{[en|enter]}} {{container_id}}`

- Create a container from template with 4GB size:

`pct {{[cr|create]}} {{container_id}} {{local:vztmpl/distro-name.tar.zst}} --rootfs {{local-lvm}}:4`

- Resize the container's disk to 20G:

`pct {{[resi|resize]}} {{container_id}} {{rootfs|mpX}} {{20G}}`

- Show the configuration of a container, specifying its ID:

`pct {{[conf|config]}} {{container_id}}`

- Snapshot a specific container with description:

`pct {{[sn|snapshot]}} {{container_id}} {{my-snapshot}} --description {{My snapshot description}}`

- Destroy a container and remove all related resources:

`pct {{[des|destroy]}} {{container_id}} --purge`
