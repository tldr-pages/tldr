# qm importdisk

> Import disk image to a VM as unused disk.
> The image format has to be supported by qemu-img(1) such as raw, qcow2, qed, vdi, vmdk, vhd.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Import a VMDK disk image to storage called "local-zfs":

`qm importdisk {{100}} name-of-disk.vmdk local-zfs`

- Import a VMDK disk image to storage called "local-lvm" as qcow2 format:

`qm importdisk {{100}} name-of-disk.vmdk local-lvm --format qcow2`
