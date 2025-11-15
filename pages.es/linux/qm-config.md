# qm config

> Muestra la configuración de la máquina virtual con los cambios de configuración pendientes aplicados.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Muestra la configuración de la máquina virtual:

`qm config {{id_mv}}`

- Muestra los valores de configuración actuales en lugar de los valores pendientes en la máquina virtual:

`qm config --current {{true}} {{id_mv}}`

- Obtiene los valores de configuración de la instantánea (snapshot) dada:

`qm config --snapshot {{nombre_de_la_instantánea}} {{id_mv}}`
