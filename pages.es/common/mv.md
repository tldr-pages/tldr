# mv

> Mueve o renombra archivos y directorios.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html>.

- Cambia el nombre de un archivo o directorio cuando el destino no es un directorio existente:

`mv {{ruta/a/origen}} {{ruta/a/destino}}`

- Mueve un archivo o directorio a un directorio existente:

`mv {{ruta/a/origen}} {{ruta/a/directorio_existente}}`

- Mueve varios archivos a un directorio existente, manteniendo los nombres de archivo sin cambios:

`mv {{ruta/a/origen1 ruta/a/origen2 ...}} {{ruta/a/directorio_existente}}`

- No pedir confirmación antes de sobrescribir los archivos existentes:

`mv {{[-f|--force]}} {{ruta/a/origen}} {{ruta/a/destino}}`

- Pedir confirmación interactivamente antes de sobrescribir archivos existentes, independientemente de los permisos de los archivos:

`mv {{[-i|--interactive]}} {{ruta/a/origen}} {{ruta/a/destino}}`

- No sobrescribir los archivos existentes en el destino:

`mv {{[-n|--no-clobber]}} {{ruta/a/origen}} {{ruta/a/destino}}`

- Mueve archivos en modo verboso, mostrando los archivos después de moverlos:

`mv {{[-v|--verbose]}} {{ruta/a/origen}} {{ruta/a/destino}}`

- Especifica el directorio de destino para poder utilizar herramientas externas para recopilar archivos movibles:

`{{find /var/log -type f -name '*.log' -print0}} | {{xargs -0}} mv {{[-t|--target-directory]}} {{ruta/a/directorio_destino}}`
