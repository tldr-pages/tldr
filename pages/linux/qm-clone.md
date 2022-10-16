# qm clone

> Create a copy of virtual machine on QEMU/KVM Virtual Machine Manager.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Copy a virtual machine:

`qm copy {{vm_id}} {{new_vm_id}}`

- Copy a virtual machine using a specific name:

`qm copy {{vm_id}} {{new_vm_id}} --name {{name}}`

- Copy a virtual machine using a specific descriptionn:

`qm copy {{vm_id}} {{new_vm_id}} --description {{description}}`

- Copy a virtual machine creating a full copy of all disks:

`qm copy {{vm_id}} {{new_vm_id}} --full`

- Copy a virtual machine using a specific format for file storage (requires `--full`):

`qm copy {{vm_id}} {{new_vm_id}} --full --format {{qcow2|raw|vmdk}}`

- Copy a virtual machine then add it to a specific pool:

`qm copy {{vm_id}} {{new_vm_id}} --pool {{pool_name}}`
