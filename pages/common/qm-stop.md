# qm stop

> Stop virtual machine.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Stop virtual machine immediately:

`qm stop {{VM_ID}}`

- Stop virtual machine and wait for at most 10 seconds:

`qm stop --timeout {{10}} {{VM_ID}}`

- Stop virtual machine and skip lock (only root can use this option):

`qm stop --skiplock {{true}} {{VM_ID}}`

- Stop virtual machine and do not deactivate storage volumes:

`qm stop --keepActive {{true}} {{VM_ID}}`
