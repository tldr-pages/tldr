# qm reboot

> Reinicia una máquina virtual cerrándola, y arrancando de nuevo después de aplicar cambios pendientes.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Reinicia una máquina virtual:

`qm reboot {{id_mv}}`

- Reinicia una máquina virtual después de esperar por lo menos 10 segundos:

`qm reboot --timeout {{10}} {{id_mv}}`
