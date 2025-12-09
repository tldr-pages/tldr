# qm stop

> Detiene una máquina virtual.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_stop>.

- Detiene una máquina virtual inmediatamente:

`qm stop {{VM_ID}}`

- Detiene una máquina virtual y espera por lo menos 10 segundos:

`qm stop --timeout {{10}} {{VM_ID}}`

- Detiene una máquina virtual y omite cualquier bloqueo (solo el root puede usar esta opción):

`qm stop --skiplock {{true}} {{VM_ID}}`

- Detiene una máquina virtual y no desactive los volúmenes de almacenamiento:

`qm stop --keepActive {{true}} {{VM_ID}}`
