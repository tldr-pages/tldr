# qm shutdown

> Apaga una máquina virtual del administrador de máquinas virtuales QEMU/KVM.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_shutdown>.

- Apaga una máquina virtual:

`qm shutdown {{VM_ID}}`

- Apaga una máquina virtual después de esperar por lo menos 10 segundos:

`qm shutdown --timeout {{10}} {{VM_ID}}`

- Apaga una máquina virtual y no desactiva los volúmenes de almacenamiento:

`qm shutdown --keepActive {{true}} {{VM_ID}}`

- Apaga una máquina virtual y omite cualquier bloqueo (solo el root puede usar esta opción):

`qm shutdown --skiplock {{true}} {{VM_ID}}`

- Detiene y apaga una máquina virtual:

`qm shutdown --forceStop {{true}} {{VM_ID}}`
