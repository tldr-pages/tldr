# qm sendkey

> Send the Qemu monitor encoding key event to the virtual machine.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Send the specified key event to the virtual machine:

`qm sendkey {{vm_id}} {{key}}`

- Allow root user to send key event and ignore locks:

`qm sendkey --skiplock {{true}} {{vm_id}} {{key}}`
