# qm guest passwd

> Sets the password for the given user on QEMU/KVM Virtual Machine Manager.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Set the password for the provided user in a vm:

`qm guest passwd {{100}} {{username}}`

- Specify if the password has already been encrypted using crypt():

`qm guest passwd {{100}} {{username}} --crypted 1`
