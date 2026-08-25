# qm sendkey

> Send QEMU monitor encoding key event to a virtual machine.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_sendkey>.

- Send the specified key event to a specific virtual machine:

`qm {{[sen|sendkey]}} {{100}} {{key}}`

- Allow root user to send key event and ignore locks:

`qm {{[sen|sendkey]}} --skiplock {{true}} {{100}} {{key}}`
