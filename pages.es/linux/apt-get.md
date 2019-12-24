# apt-get

> Herramienta de gestión de paquete para distribuciones basadas en Debian.
> Buscar paquetes utilizando `apt-cache`.

- Actualiza la lista de paquetes y versiones disponibles (se recomienda ejecutar este comando antes que cualquier otro comando `apt-get`):

`apt-get update`

- Instala un paquete o actualizarlo a su última versión disponible:

`apt-get install {{paquete}}`

- Elimina un paquete:

`apt-get remove {{paquete}}`

- Elimina un paquete y sus archivos de configuración:

`apt-get purge {{paquete}}`

- Actualizar todos los paquetes instalados a sus nuevas versiones disponibles:

`apt-get upgrade`

- Eliminar todos los paquetes innecesarios:

`apt-get autoremove`

- Actualiza paquetes instalados (como `upgrade`), pero elimina paquete obsoletos e instala paquetes adiciones para satisfacer nuevas dependencias:

`apt-get dist-upgrade`
