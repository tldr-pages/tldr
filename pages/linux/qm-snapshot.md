# qm snapshot

> Create virtual machine snapshots.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_snapshot>.

- Create a snapshot of a specific virtual machine (name must start with a letter):

`qm {{[sn|snapshot]}} {{vm_id}} {{snapshot_name}}`

- Create a snapshot with a specific description:

`qm {{[sn|snapshot]}} {{vm_id}} {{snapshot_name}} --description {{description}}`

- Create a snapshot including the vmstate:

`qm {{[sn|snapshot]}} {{vm_id}} {{snapshot_name}} --description {{description}} --vmstate 1`

- List snapshots of a VM:

`qm {{[lists|listsnapshot]}} {{100}}`

- Rollback the state of a specific VM to a specified snapshot:

`qm {{[ro|rollback]}} {{vm_id}} {{snap_name}}`
