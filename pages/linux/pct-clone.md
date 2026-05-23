# pct clone

> Clone a container.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_clone>.

- Clone a container:

`pct {{[cl|clone]}} {{container_id}} {{new_container_id}}`

- Clone a container with a custom name:

`pct {{[cl|clone]}} {{container_id}} {{new_container_id}} --hostname {{host_name}}`

- Create a full clone instead of a linked clone:

`pct {{[cl|clone]}} {{container_id}} {{new_container_id}} --full`
