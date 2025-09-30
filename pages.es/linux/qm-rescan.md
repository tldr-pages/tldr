# qm rescan

> Revisa de nuevo (rescan) todos los almacenamientos (storages) y actualiza los tamaños de discos e imágenes de disco no utilizadas de una máquina virtual.
> Más información: <https://pve.proxmox.com/pve-docs/qm.1.html>.

- Restaura todos los almacenamientos y actualiza los tamaños de disco e imágenes de disco no utilizadas de la máquina virtual indicada:

`qm rescan {{id_mv}}`

- Realiza una simulación de rescan en una máquina virtual específica y no escribe ningún cambio en las configuraciones:

`qm rescan --dryrun {{true}} {{id_mv}}`
