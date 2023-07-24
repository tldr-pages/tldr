# qm disk move

> Move a virtual disk from one storage to another within the same Proxmox cluster.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Move a virtual disk:

`qm disk move {{vm_id}} {{destination}} {{index}}`

- Delete the previous copy of the virtual disk:

`qm disk move -delete {{vm_id}} {{destination}} {{index}}`
