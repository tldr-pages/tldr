# qm destroy

> Destroy a virtual machine in QEMU/KVM Virtual Machine Manager.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Destroy a specific virtual machine:

`qm destroy {{vm_id}}`

- Destroy all disks that are not explicitly referenced in a specific virtual machine's configuration:

`qm destroy {{vm_id}} --destroy-unreferenced-disks`

- Destroy a virtual machine and remove from all locations (inventory, backup jobs, high availability managers, etc.):

`qm destroy {{vm_id}} --purge`

- Destroy a specific virtual machine ignoring locks and forcing destroy:

`sudo qm destroy {{vm_id}} --skiplock`
