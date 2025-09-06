# qm migrate

> Migra una máquina virtual.
> Se usa para crear una nueva tarea de migración.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Migra una máquina virtual específica:

`qm migrate {{id_mv}} {{destino}}`

- Supera el límite de ancho de banda E/S actual con 10 KiB/s:

`qm migrate {{id_mv}} {{destino}} --bwlimit 10`

- Permite la migración de máquinas virtuales usando dispositivos locales (solo root):

`qm migrate {{id_mv}} {{destino}} --force true`

- Utiliza la migración en vivo (online) si una máquina virtual está ejecutándose:

`qm migrate {{id_mv}} {{destino}} --online true`

- Permite la migración de almacenamiento en vivo para discos locales:

`qm migrate {{id_mv}} {{destino}} --with-local-disks true`
