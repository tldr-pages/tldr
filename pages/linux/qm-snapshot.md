# qm snapshot

> Create virtual machine snapshots.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Create a snapshot of a specific virtual machine:

`qm snapshot {{vm_id}} {{snapshot_name}}`

- Give a textual description or comment:

`qm snapshot {{vm_id}} {{snapshot_name}} --description {{description}}`

- Save the vmstate:

`qm snapshot {{vm_id}} {{snapshot_name}} --description {{description}} --vmstate 1`
