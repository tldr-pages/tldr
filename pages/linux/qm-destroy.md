# qm destroy

> Destroy a virtual machine (VM) in QEMU/KVM Virtual Machine Manager.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Destroy a specific VM:

`qm destroy {{vm_id}}`

- Destroy all disks with the same VMID that are not explicitly referenced in the configuration:

`qm destroy {{vm_id}} --destroy-unreferenced-disks`

- Remove VMID from all configurations such as backup & replication jobs:

`qm destroy {{vm_id}} --purge`

- Ignore locks and force destroy - must be run as root:

`qm destroy {{vm_id}} --skiplock`
