# debman

> Lee las páginas de ayuda (man) de paquetes desinstalados.
> Más información: <https://manned.org/debman.1>.

- Lee una página man para un comando proporcionado por un paquete dado:

`debman -p {{paquete}} {{comando}}`

- Especifica una versión de paquete a descargar:

`debman -p {{paquete}}={{versión}} {{comando}}`

- Lee una página man de un archivo `.deb`:

`debman -f {{ruta/al/archivoname.deb}} {{comando}}`
