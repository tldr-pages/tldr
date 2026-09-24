# qm shutdown

> Shut down a virtual machine on QEMU/KVM Virtual Machine Manager.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_shutdown>.

- Shut down a virtual machine:

`qm {{[shu|shutdown]}} {{100}}`

- Shut down a virtual machine after wait for at most 10 seconds:

`qm {{[shu|shutdown]}} {{100}} --timeout 10`

- Shut down a virtual machine and do not deactivate storage volumes:

`qm {{[shu|shutdown]}} {{100}} --keepActive true`

- Shut down a virtual machine and skip lock (only root can use this option):

`qm {{[shu|shutdown]}} {{100}} --skiplock true`

- Stop and shut down a virtual machine:

`qm {{[shu|shutdown]}} {{100}} --forceStop true`
