# qm disk move

> Mueve un disco virtual de un almacenamiento a otro dentro del mismo grupo Proxmox.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Mueve un disco virtual:

`qm disk move {{vm_id}} {{destino}} {{índice}}`

- Elimina la copia anterior del disco virtual:

`qm disk move -delete {{vm_id}} {{destino}} {{índice}}`
