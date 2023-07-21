# qm move_disk Command

> Move a virtual disk from one storage to another within the same Proxmox cluster.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- To move a virtual disk:

`qm move_disk {{id}} {{destination}} {{index}}`

- To delete the previous copy of virtual disk:

`qm move_disk -delete {{id}} {{destination}} {{index}}`
