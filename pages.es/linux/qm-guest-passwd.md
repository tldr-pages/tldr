# qm guest passwd

> Establece la contraseña para un usuario en el administrador de máquinas virtuales QEMU/KVM.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Establece una contraseña para un usuario específico en una máquina virtual de forma interactiva:

`qm guest passwd {{id_mv}} {{usuario}}`

- Establece una contraseña ya procesada (hashed) para un usuario específico en una máquina virtual de forma interactiva:

`qm guest passwd {{id_mv}} {{usuario}} --crypted 1`
