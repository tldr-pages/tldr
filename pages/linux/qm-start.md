# qm start

> Start a virtual machine on QEMU/KVM Virtual Machine Manager.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_start>.

- Start a specific virtual machine:

`qm start {{vm_id}}`

- Specify the QEMU machine type (i.e. the CPU to emulate):

`qm start {{vm_id}} --machine {{q35}}`

- Start a specific virtual machine with a timeout in 60 seconds:

`qm start {{vm_id}} --timeout {{60}}`
