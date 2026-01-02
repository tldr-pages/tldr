# qm reset

> Reset a virtual machine on QEMU/KVM Virtual Machine Manager.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_reset>.

- Reset a virtual machine:

`qm reset {{vm_id}}`

- Reset a virtual machine and skip lock (only root can use this option):

`qm reset --skiplock {{true}} {{vm_id}}`
