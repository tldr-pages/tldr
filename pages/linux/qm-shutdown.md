# qm shutdown

> Shutdown a virtual machine on QEMU/KVM Virtual Machine Manager.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_shutdown>.

- Shutdown a virtual machine:

`qm {{[shu|shutdown]}} {{100}}`

- Shutdown a virtual machine after wait for at most 10 seconds:

`qm {{[shu|shutdown]}} --timeout {{10}} {{100}}`

- Shutdown a virtual machine and do not deactivate storage volumes:

`qm {{[shu|shutdown]}} --keepActive {{true}} {{100}}`

- Shutdown a virtual machine and skip lock (only root can use this option):

`qm {{[shu|shutdown]}} --skiplock {{true}} {{100}}`

- Stop and shutdown a virtual machine:

`qm {{[shu|shutdown]}} --forceStop {{true}} {{100}}`
