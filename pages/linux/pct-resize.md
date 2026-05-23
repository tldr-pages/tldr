# pct resize

> Resize container storage.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_resize>.

- Resize the container size to 20GB:

`pct {{[resi|resize]}} {{container_id}} rootfs 20G`

- Add 10GB to the container storage:

`pct {{[resi|resize]}} {{container_id}} rootfs +10G`

- Resize a mounted volume:

`pct {{[resi|resize]}} {{container_id}} mp{{0}} {{+10G}}`
