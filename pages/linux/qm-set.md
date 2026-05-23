# qm set

> Set virtual machine options.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_set>.

- Set a name for a VM in the GUI:

`qm set {{vm_id}} --name {{vm_name}}`

- Set a VM to autostart on boot:

`qm set {{vm_id}} --autostart {{0|1}}`

- Set the allotted core count of a VM:

`qm set {{vm_id}} --cores {{4}}`

- Set the allotted amount of memory:

`qm set {{vm_id}} --memory {{8192}}`

- Give a VM a network device and bridge it to the host network:

`qm set {{vm_id}} --net{{0}} {{virtio|e1000|rtl8139|vmxnet3}},bridge=vmbr{{0}}`

- Delete a device:

`qm set {{vm_id}} --delete {{device_name0,device_name1,...}}`

- Passthrough a GPU device to the guest:

`qm set {{vm_id}} --hostpci{{0}} {{0000:00:02}},x-vga=1 --bios ovmf`
