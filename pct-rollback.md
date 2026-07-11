# pct rollback

> Restore a specific snapshot.
> More information: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_rollback>.

- Restore a snapshot:

`pct rollback {{100}} {{snapshot_name}}`

- Start the container as soon as the snapshot is restored:

`pct rollback {{100}} {{snapshot_name}} --start`
