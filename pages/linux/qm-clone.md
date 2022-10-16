# qm clone

> Create a copy of virtual machine on QEMU/KVM Virtual Machine Manager.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Copy a virtual machine:

`qm copy {{100}} {{102}}`

- Set a name for the cloned VM:

`qm copy {{100}} {{102}} --name {{name}}`

- Set a description for the cloned VM:

`qm copy {{100}} {{102}} --description {{description}}`

- Create a full clone of the source VM:

`qm copy {{100}} {{102}} --full`

- Specify file format for the cloned VM (requires full clone):

`qm copy {{100}} {{102}} --full --format {{qcow2 | raw | vmdk}}`

- Specify pool for the cloned VM:

`qm copy {{100}} {{102}} --pool {{pool_name}}`
