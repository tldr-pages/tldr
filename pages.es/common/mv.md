# mv

> Mueve o renombra archivos y directorios.
> Más información: <https://www.gnu.org/software/coreutils/mv>.

- Cambia el nombre de un archivo o directorio cuando el destino no es un directorio existente:

`mv {{ruta/a/origen}} {{ruta/a/destino}}`

- Mueve un archivo o directorio a un directorio existente:

`mv {{ruta/a/origen}} {{ruta/a/directorio_existente}}`

- Mueve varios archivos a un directorio existente, manteniendo los nombres de archivo sin cambios:

`mv {{ruta/a/origen1 ruta/a/origen2 ...}} {{ruta/a/directorio_existente}}`

- No pedir confirmación ([f]) antes de sobrescribir los archivos existentes:

`mv --force {{ruta/a/origen}} {{ruta/a/destino}}`

- Pedir confirmación [i]nteractivamente antes de sobrescribir archivos existentes, independientemente de los permisos de los archivos:

`mv --interactive {{ruta/a/origen}} {{ruta/a/destino}}`

- No sobrescribir ([n]) los archivos existentes en el destino:

`mv --no-clobber {{ruta/a/origen}} {{ruta/a/destino}}`

- Mueve archivos en modo [v]erbose, mostrando los archivos después de moverlos:

`mv --verbose {{ruta/a/origen}} {{ruta/a/destino}}`

- Especifica el directorio de des[t]ino para poder utilizar herramientas externas para recopilar archivos movibles:

`{{find /var/log -type f -name '*.log' -print0}} | {{xargs -0}} mv --target-directory {{ruta/a/directorio_destino}}`
