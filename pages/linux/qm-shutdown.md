# qm shutdown

> Shutdown a virtual machine on QEMU/KVM Virtual Machine Manager.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Shutdown a virtual machine:

`qm shutdown {{VM_ID}}`

- Shutdown a virtual machine after wait for at most 10 seconds:

`qm shutdown --timeout {{10}} {{VM_ID}}`

- Shutdown a virtual machine and do not deactivate storage volumes:

`qm shutdown --keepActive {{true}} {{VM_ID}}`

- Shutdown a virtual machine and skip lock (only root can use this option):

`qm shutdown --skiplock {{true}} {{VM_ID}}`

- Stop and shutdown a virtual machine:

`qm shutdown --forceStop {{true}} {{VM_ID}}`
