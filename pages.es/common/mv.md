# mv

> Mueve o renombra archivos y directorios.

- Mueve archivos en ubicaciones arbitrarias:

`mv {{origen}} {{destino}}`

- Mueve sin solicitar confirmación antes de sobrescribir archivos existentes:

`mv -f {{origen}} {{destino}}`

- Solicita confirmación antes de sobrescribir archivos existentes, independientemente de los permisos del archivo:

`mv -i {{origen}} {{destino}}`

- No sobrescribe archivos existentes en el destino:

`mv -n {{origen}} {{destino}}`

- Mueve archivos en modo detallado, mostrando los archivos después de moverlos:

`mv -v {{origen}} {{destino}}`
