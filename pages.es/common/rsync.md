# rsync

> Transfiere archivos hacia o desde un host remoto (pero no entre dos hosts remotos), usando SSH por defecto.
> Para especificar una ruta remota, usa `usuario@host:ruta/al/archivo_o_directorio`.
> Más información: <https://download.samba.org/pub/rsync/rsync.1>.

- Transfiere un archivo (usa `--dry-run` para simular la transferencia):

`rsync {{ruta/al/origen}} {{ruta/al/destino}}`

- Usa el modo archivo (copia directorios recursivamente, copia enlaces simbólicos sin resolverlos y preserva permisos, propiedad y marcas de tiempo):

`rsync {{[-a|--archive]}} {{ruta/al/origen}} {{ruta/al/destino}}`

- Comprime los datos al enviarlos al destino, muestra el progreso detallado y legible, y conserva los archivos parcialmente transferidos si se interrumpe:

`rsync {{[-zvhP|--compress --verbose --human-readable --partial --progress]}} {{ruta/al/origen}} {{ruta/al/destino}}`

- Copia directorios recursivamente y garantiza que cada archivo esté completamente guardado en disco en lugar de permanecer en RAM:

`rsync {{[-r|--recursive]}} --fsync {{ruta/al/origen}} {{ruta/al/destino}}`

- Transfiere el contenido de un directorio, pero no el directorio en sí:

`rsync {{[-r|--recursive]}} {{ruta/al/origen}}/ {{ruta/al/destino}}`

- Usa el modo archivo, resuelve enlaces simbólicos y omite archivos que sean más recientes en el destino:

`rsync {{[-auL|--archive --update --copy-links]}} {{ruta/al/origen}} {{ruta/al/destino}}`

- Transfiere un directorio desde un host remoto que ejecuta `rsyncd` y elimina archivos en el destino que no existen en el origen:

`rsync {{[-r|--recursive]}} --delete rsync://{{host}}:{{ruta/al/origen}} {{ruta/al/destino}}`

- Transfiere un archivo a través de SSH usando un puerto diferente al predeterminado (22) y muestra el progreso global:

`rsync {{[-e|--rsh]}} 'ssh -p {{puerto}}' --info=progress2 {{host}}:{{ruta/al/origen}} {{ruta/al/destino}}`
