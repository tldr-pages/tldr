# qm sendkey

> Envía un evento de teclado del monitor QEMU a una máquina virtual.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_sendkey>.

- Envía el evento de teclado (key) especificado a una máquina virtual específica:

`qm {{[sen|sendkey]}} {{id_mv}} {{tecla}}`

- Permite al usuario root enviar el evento clave e ignorar cualquier bloqueo:

`qm {{[sen|sendkey]}} --skiplock {{true}} {{id_mv}} {{tecla}}`
