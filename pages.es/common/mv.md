# mv

> Mueve o renombra archivos y directorios.
> Más información: <https://www.gnu.org/software/coreutils/mv>.

- Mueve archivos en ubicaciones arbitrarias:

`mv {{ruta/al/origen}} {{ruta/al/destino}}`

- Mueve sin solicitar confirmación antes de sobrescribir archivos existentes:

`mv -f {{ruta/al/origen}} {{ruta/al/destino}}`

- Solicita confirmación antes de sobrescribir archivos existentes, independientemente de los permisos del archivo:

`mv -i {{ruta/al/origen}} {{ruta/al/destino}}`

- Mueve un archivo sin sobreescribir otro archivo:

`mv -n {{ruta/al/origen}} {{ruta/al/destino}}`

- Mueve archivos en modo detallado, mostrando los archivos después de moverlos:

`mv -v {{ruta/al/origen}} {{ruta/al/destino}}`
