# qm stop

> Detiene una máquina virtual.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_stop>.

- Detiene una máquina virtual inmediatamente:

`qm stop {{100}}`

- Detiene una máquina virtual y espera por lo menos 10 segundos:

`qm stop {{100}} --timeout {{10}}`

- Detiene una máquina virtual y omite cualquier bloqueo (solo el root puede usar esta opción):

`qm stop {{100}} --skiplock {{true}}`

- Detiene una máquina virtual y no desactive los volúmenes de almacenamiento:

`qm stop {{100}} --keepActive {{true}}`
