# qm resume

> Resume a virtual machine.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Resume a specific virtual machine:

`qm resume {{vm_id}}`

- Resume a specific virtual machine ignoring locks (requires root):

`sudo qm resume {{vm_id}} --skiplock true`
