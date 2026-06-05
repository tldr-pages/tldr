# pct move-volume

> Mueve un volumen a un almacenamiento diferente o a un contenedor diferente.
> Más información: <https://pve.proxmox.com/pve-docs/pct.1.html#cli_pct_move-volume>.

- Mueve el sistema de archivos raíz de un contenedor a un almacenamiento diferente:

`pct {{[mov|move-volume]}} {{100}} rootfs {{storage_id}}`

- Elimina la asociación del sistema de archivos con el volumen anterior una vez completado el traslado:

`pct {{[mov|move-volume]}} {{100}} rootfs {{storage_id}} --delete`
