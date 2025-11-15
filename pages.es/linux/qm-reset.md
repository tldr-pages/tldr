# qm reset

> Reinicia una máquina virtual en el administrador de máquinas virtuales QEMU/KVM.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Restablece una máquina virtual:

`qm reset {{id_mv}}`

- Reinicia una máquina virtual y omite cualquier bloqueo (solo el root puede usar esta opción):

`qm reset --skiplock {{true}} {{id_mv}}`
