# mv

> Mover o renombra archivos y directorios.

- Mover archivos en ubicaciones arbitrarias:

`mv {{origen}} {{destino}}`

- Mover sin solicitar confirmación antes de sobrescribir archivos existentes:

`mv -f {{origen}} {{destino}}`

- Solicitar confirmación antes de sobrescribir archivos existentes, independientemente de los permisos del archivo:

`mv -i {{origen}} {{destino}}`

- No sobrescribir archivos existentes en el destino:

`mv -n {{origen}} {{destino}}`

- Mover archivos en modo detallado, mostrando los archivos después de moverlos:

`mv -v {{origen}} {{destino}}`
