# qm snapshot

> Crea instantáneas de máquinas virtuales.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Crea una instantánea de una máquina virtual dada:

`qm snapshot {{id_mv}} {{nombre_de_la_instantánea}}`

- Crea una instantánea con una descripción dada:

`qm snapshot {{id_mv}} {{nombre_de_la_instantánea}} --description {{descripción}}`

- Crea una instantánea incluyendo el vmstate:

`qm snapshot {{id_mv}} {{nombre_de_la_instantánea}} --description {{descripción}} --vmstate 1`
