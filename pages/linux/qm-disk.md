# qm disk

> Manage disk images.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_disk_import>.

- Add `n` gigabytes to a virtual disk:

`qm {{[di|disk]}} {{[resi|resize]}} {{vm_id}} {{disk_name}} +{{n}}G`

- Move a virtual disk:

`qm {{[di|disk]}} {{[m|move]}} {{vm_id}} {{destination}} {{index}}`

- Delete the previous copy of the virtual disk:

`qm {{[di|disk]}} {{[m|move]}} --delete {{vm_id}} {{destination}} {{index}}`

- Import a VMDK/qcow2/raw disk image using a specific storage name:

`qm {{[di|disk]}} {{[i|import]}} {{vm_id}} {{path/to/disk}} {{storage_name}} --format {{qcow2|raw|vmdk}}`
