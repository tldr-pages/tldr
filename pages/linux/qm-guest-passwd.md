# qm guest passwd

> Set the password for a specific user on QEMU/KVM Virtual Machine Manager.
> More information: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Set the password for a specific user in a virtual machine:

`qm guest passwd {{vm_id}} {{username}}`

- Specify if the password has already been encrypted using crypt():

`qm guest passwd {{vm_id}} {{username}} --crypted 1`
