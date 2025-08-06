# qm set

> Set virtual machine options.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Set a name for a VM in the GUI:

`qm set {{100}} --name {{vm_name}}`

- Set a VM to autostart on boot:

`qm set {{100}} --autostart {{0|1}}`

- Set the allotted core count of a VM:

`qm set {{100}} --cores {{4}}`

- Set the allotted amount of memory:

`qm set {{100}} --memory {{8192}}`

- Give a VM a network device and bridge it to the host network:

`qm set {{100}} --net{{0}} {{virtio|e1000|rtl8139|vmxnet3}},bridge=vmbr{{0}}`

- Delete a device:

`qm set {{100}} --delete {{device_name0}}`
