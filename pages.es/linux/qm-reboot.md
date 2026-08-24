# qm reboot

> Reinicia una máquina virtual cerrándola, y arrancando de nuevo después de aplicar cambios pendientes.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_reboot>.

- Reinicia una máquina virtual:

`qm {{[reb|reboot]}} {{100}}`

- Reinicia una máquina virtual después de esperar por lo menos 10 segundos:

`qm {{[reb|reboot]}} {{100}} --timeout {{10}}`
