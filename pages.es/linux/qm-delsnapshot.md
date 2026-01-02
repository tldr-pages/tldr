# qm delsnapshot

> Elimina instantáneas (snapshots) de máquinas virtuales.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_delsnapshot>.

- Elimina una instantánea:

`qm delsnapshot {{id_mv}} {{nombre_de_la_instantánea}}`

- Elimina una instantánea de un archivo de configuración (incluso si la eliminación del disco de la instantánea falla):

`qm delsnapshot {{id_mv}} {{nombre_de_la_instantánea}} --force 1`
