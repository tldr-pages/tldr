# qm resume

> Resume a virtual machine.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Resume a specific virtual machine:

`qm resume {{vm_id}}`

- Ignore locks when resuming a specific virtual machine (root only):

`qm resume {{vm_id}} --skiplock true`
