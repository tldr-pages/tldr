# qm clone

> Create a copy of virtual machine on QEMU/KVM Virtual Machine Manager.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_clone>.

- Copy a virtual machine:

`qm clone {{100}} {{101}}`

- Copy a virtual machine using a specific name:

`qm clone {{100}} {{101}} --name {{name}}`

- Copy a virtual machine using a specific descriptionn:

`qm clone {{100}} {{101}} --description {{description}}`

- Copy a virtual machine creating a full copy of all disks:

`qm clone {{100}} {{101}} --full`

- Copy a virtual machine using a specific format for file storage (requires `--full`):

`qm clone {{100}} {{101}} --full --format {{qcow2|raw|vmdk}}`

- Copy a virtual machine then add it to a specific pool:

`qm clone {{100}} {{101}} --pool {{pool_name}}`
