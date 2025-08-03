# qm set

> Set virtual machine options.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Set a name for a VM in the GUI:

`wm set {{100}} --name {{vm_name}}`

- Set a VM to autostart on boot:

`wm set {{100}} --autostart {{0|1}}`

- Set the alotted core count of a VM:

`wm set {{100}} --cores {{4}}`
