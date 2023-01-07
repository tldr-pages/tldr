# qm sendkey

> Send QEMU monitor encoding key event to a virtual machine.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Send the specified key event to a specific virtual machine:

`qm sendkey {{vm_id}} {{key}}`

- Allow root user to send key event and ignore locks:

`qm sendkey --skiplock {{true}} {{vm_id}} {{key}}`
