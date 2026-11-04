# pct fsck

> Run a filesystem check on a container volume.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_fsck>.

- Check all volumes of a container:

`pct fsck {{100}}`

- Specify which volume to check:

`pct fsck {{100}} --device {{mp0|mp1|rootfs|...}}`
