# pct move-volume

> Move a volume to a different storage or to a different container.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_move-volume>.

- Move the root filesystem of a container to a different storage:

`pct {{[mov|move-volume]}} {{100}} rootfs {{storage_id}}`

- Delete the filesystem association once the move is complete:

`pct {{[mov|move-volume]}} {{100}} rootfs {{storage_id}} --delete`
