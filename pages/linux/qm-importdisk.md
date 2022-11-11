# qm importdisk

> Import disk image to a VM as unused disk.
> The image format has to be supported by `qemu-img` such as raw, qcow2, qed, vdi, vmdk, vhd.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Import a VMDK disk image to specific storage:

`qm importdisk {{100}} {{path/to/disk.vmdk}} {{storage_name}}`

- Import a VMDK disk image to specific storage in a specific format:

`qm importdisk {{vm_id}} {{path/to/disk.vmdk}} {{storage_name}} --format {{qcow2 | raw | vmdk}}`
