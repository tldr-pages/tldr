# qm importdisk

> Import disk image to a VM as unused disk.
> The supported image formats for qemu-img, such as raw, qcow2, qed, vdi, vmdk, and vhd, must be used.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Import a VMDK disk image to specific storage:

`qm importdisk {{100}} {{path/to/disk.vmdk}} {{storage_name}}`

- Import a VMDK disk image to specific storage in a specific format:

`qm importdisk {{vm_id}} {{path/to/disk.vmdk}} {{storage_name}} --format {{qcow2|raw|vmdk}}`
