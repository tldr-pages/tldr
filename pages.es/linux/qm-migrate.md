# qm migrate

> Migra una máquina virtual.
> Se usa para crear una nueva tarea de migración.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_migrate>.

- Migra una máquina virtual específica:

`qm {{[mi|migrate]}} {{100}} {{destino}}`

- Supera el límite de ancho de banda E/S actual con 10 KiB/s:

`qm {{[mi|migrate]}} {{100}} {{destino}} --bwlimit 10`

- Permite la migración de máquinas virtuales usando dispositivos locales (solo root):

`qm {{[mi|migrate]}} {{100}} {{destino}} --force true`

- Utiliza la migración en vivo (online) si una máquina virtual está ejecutándose:

`qm {{[mi|migrate]}} {{100}} {{destino}} --online true`

- Permite la migración de almacenamiento en vivo para discos locales:

`qm {{[mi|migrate]}} {{100}} {{destino}} --with-local-disks true`
