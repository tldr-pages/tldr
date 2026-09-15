# qm disk

> Manage disk images.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_disk_import>.

- Add `n` gigabytes to a virtual disk:

`qm {{[di|disk]}} {{[resi|resize]}} {{100}} {{disk_name}} +{{n}}G`

- Move a virtual disk:

`qm {{[di|disk]}} {{[m|move]}} {{100}} {{scic0}} {{destination_storage_name}}`

- Delete the previous copy of the virtual disk:

`qm {{[di|disk]}} {{[m|move]}} {{100}} {{scic0}} {{destination_storage_name}} --delete`

- Import a VMDK/`.qcow2`/raw disk image using a specific storage name:

`qm {{[di|disk]}} {{[i|import]}} {{100}} {{path/to/disk}} {{storage_name}} --format {{qcow2|raw|vmdk}}`

- Rescan all storages and update disk sizes and unused disk images:

`qm {{[di|disk]}} {{[resc|rescan]}}`

- Perform a dry-run of a rescan and do not write any changes to configurations:

`qm {{[di|disk]}} {{[resc|rescan]}} --dryrun`

- Specify a virtual machine by its ID:

`qm {{[di|disk]}} {{[resc|rescan]}} --vmid {{100}}`

- Delete a disk:

`qm {{[di|disk]}} {{[u|unlink]}} {{100}} --idlist {{unused0,unused1,scsi1,...}}`
