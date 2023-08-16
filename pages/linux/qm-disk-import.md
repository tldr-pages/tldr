# qm disk import

> Import a disk image to a virtual machine as an unused disk.
> The supported image formats for `qemu-img`, such as raw, qcow2, qed, vdi, vmdk, and vhd must be used.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Import a VMDK/qcow2/raw disk image using a specific storage name:

`qm importdisk {{vm_id}} {{path/to/disk}} {{storage_name}} --format {{qcow2|raw|vmdk}}`
