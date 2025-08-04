# qm set

> Set virtual machine options.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Set a name for a VM in the GUI:

`qm set {{100}} --name {{vm_name}}`

- Set a VM to autostart on boot:

`qm set {{100}} --autostart {{0|1}}`

- Set the alotted core count of a VM:

`qm set {{100}} --cores {{4}}`

- Set the alotted amount of memory:

`qm set {{100}} --memory {{8192}}`
