# qm start

> Start a virtual machine on Qemu/KVM Virtual Machine Manager.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Start a specific virtual machine:
`qm start {{100}}`

- Specify the Qemu machine type (i.e. the CPU to emulate):
`qm start {{100}} --machine {{q35}}`

- Timeout if the machine doesn't start within 60 seconds:
`qm start {{100}} --timeout {{60}}`
