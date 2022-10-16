# qm cloudinit dump

> Get an automatically generated cloudinit config on QEMU/KVM Virtual Machine Manager.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Automatically generate a cloudinit config:

`qm cloudinit dump {{100}}`

- Specify the config type:

`qm cloudinit dump {{100}} {{meta | network | user}}`
