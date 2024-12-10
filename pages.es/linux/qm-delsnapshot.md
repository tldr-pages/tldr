# qm delsnapshot

> Elimina instantáneas de máquinas virtuales.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Elimina una instantánea:

`qm delsnapshot {{id_mv}} {{nombre_de_instantánea}}`

- Elimina una instantánea de un archivo de configuración (incluso si la eliminación del disco de la instantánea falla):

`qm delsnapshot {{id_mv}} {{nombre_de_instantánea}} --force 1`
