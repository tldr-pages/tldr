# qm config

> Muestra la configuración de la máquina virtual con los cambios de configuración pendientes aplicados.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html#cli_qm_config>.

- Muestra la configuración de la máquina virtual:

`qm {{[co|config]}} {{100}}`

- Muestra los valores de configuración actuales en lugar de los valores pendientes en la máquina virtual:

`qm {{[co|config]}} --current {{true}} {{100}}`

- Obtiene los valores de configuración de la instantánea (snapshot) dada:

`qm {{[co|config]}} --snapshot {{nombre_de_la_instantánea}} {{100}}`
