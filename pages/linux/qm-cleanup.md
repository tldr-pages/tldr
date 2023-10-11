# qm cleanup

> Clean up resources on QEMU/KVM Virtual Machine Manager like tap devices, VGPUs, etc.
> Called after a VM shuts down, crashes, etc.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Clean up resources:

`qm cleanup {{vm_id}} {{clean-shutdown}} {{guest-requested}}`
