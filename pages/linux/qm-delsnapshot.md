# qm delsnapshot

> Delete virtual machine snapshots.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_delsnapshot>.

- Delete a snapshot:

`qm {{[del|delsnapshot]}} {{100}} {{snapshot_name}}`

- Delete a snapshot from a configuration file (even if removing the disk snapshot fails):

`qm {{[del|delsnapshot]}} {{100}} {{snapshot_name}} --force 1`
