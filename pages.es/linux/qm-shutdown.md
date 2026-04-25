# qm shutdown

> Apaga una máquina virtual del administrador de máquinas virtuales QEMU/KVM.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_shutdown>.

- Apaga una máquina virtual:

`qm {{[shu|shutdown]}} {{100}}`

- Apaga una máquina virtual después de esperar por lo menos 10 segundos:

`qm {{[shu|shutdown]}} --timeout {{10}} {{100}}`

- Apaga una máquina virtual y no desactiva los volúmenes de almacenamiento:

`qm {{[shu|shutdown]}} --keepActive {{true}} {{100}}`

- Apaga una máquina virtual y omite cualquier bloqueo (solo el root puede usar esta opción):

`qm {{[shu|shutdown]}} --skiplock {{true}} {{100}}`

- Detiene y apaga una máquina virtual:

`qm {{[shu|shutdown]}} --forceStop {{true}} {{100}}`
