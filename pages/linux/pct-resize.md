# pct resize

> Resize container storage.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html>.

- Resize the container size to 20GB:

`pct {{[resi|resize]}} {{100}} rootfs 20G`

- Add 10GB to the container storage:

`pct {{[resi|resize]}} {{100}} rootfs +10G`
