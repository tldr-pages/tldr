# mount

> Accede a un sistema de archivos completo desde un directorio.
> Vea también: `udisksctl`.
> Más información: <https://manned.org/mount.8>.

- Muestra todos los sistemas de archivos montados:

`mount`

- Monta un dispositivo en un directorio:

`mount {{ruta/al/archivo_de_dispositivo}} {{ruta/al/directorio_destino}}`

- Crea un directorio específico si no existe y monta un dispositivo en él:

`mount {{[-m|--mkdir]}} {{ruta/al/archivo_de_dispositivo}} {{ruta/al/directorio_destino}}`

- Monta un dispositivo en un directorio para un usuario específico:

`mount {{[-o|--options]}} uid={{id_de_usuario}},gid={{id_de_grupo}} {{ruta/al/archivo_de_dispositivo}} {{ruta/al/directorio_destino}}`

- Monta un CD-ROM (con el sistema de archivos ISO9660) en `/cdrom` (solo lectura):

`mount {{[-t|--types]}} iso9660 {{[-o|--options]}} ro {{/dev/cdrom}} /cdrom`

- Monta todos los sistemas de archivos definidos en `/etc/fstab`:

`mount {{[-a|--all]}}`

- Monta un sistema de archivos específico descrito en `/etc/fstab` (por ejemplo, `/dev/sda1 /ruta/al/punto_de_montaje ext2 defaults 0 2`):

`mount {{ruta/al/punto_de_montaje}}`

- Monta un directorio en otro directorio:

`mount {{[-B|--bind]}} {{ruta/al/directorio_antiguo}} {{ruta/al/directorio_nuevo}}`
