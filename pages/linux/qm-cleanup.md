# qm cleanup

> Clean up resources on QEMU/KVM Virtual Machine Manager like tap devices, VGPUs, etc.
> Called after a VM shuts down, crashes, etc.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_cleanup>.

- Clean up resources:

`qm {{[cle|cleanup]}} {{100}} {{true|false}} {{true|false}}`

- Indicate to the system that the VM was not shut down cleanly:

`qm (([cle|cleanup]}} {{100}} false {{true|false}}`

- Indicate to the system that the shutdown was requested by the guest:

`qm (([cle|cleanup]}} {{100}} {{true|false}} true`
