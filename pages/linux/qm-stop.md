# qm stop

> Stop a virtual machine.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_stop>.

- Stop a virtual machine immediately:

`qm stop {{100}}`

- Stop a virtual machine and wait for at most 10 seconds:

`qm stop --timeout {{10}} {{100}}`

- Stop a virtual machine and skip lock (only root can use this option):

`qm stop --skiplock {{true}} {{100}}`

- Stop a virtual machine and don't deactivate storage volumes:

`qm stop --keepActive {{true}} {{100}}`
