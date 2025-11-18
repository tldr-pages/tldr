# apt-get

> Utilidad de gestión de paquetes para Debian y Ubuntu.
> Búsqueda de paquetes mediante `apt-cache`.
> Más información: <https://manned.org/apt-get.8>.

- Actualiza la lista de paquetes y versiones disponibles (se recomienda ejecutar esto antes de otros comandos `apt-get`):

`sudo apt-get update`

- Instala un paquete o lo actualiza a la última versión disponible:

`sudo apt-get install {{paquete}}`

- Elimina un paquete:

`sudo apt-get remove {{paquete}}`

- Elimina un paquete y sus archivos de configuración:

`sudo apt-get purge {{paquete}}`

- Actualiza todos los paquetes instalados a sus versiones más recientes:

`sudo apt-get upgrade`

- Limpia el repositorio local: elimina los archivos de paquetes (`.deb`) de descargas interrumpidas que ya no pueden descargarse:

`apt-get autoclean`

- Elimina todos los paquetes que ya no sean necesarios:

`sudo apt-get autoremove`

- Actualiza los paquetes instalados (como `upgrade`), pero eliminando los paquetes obsoletos e instalando paquetes adicionales para satisfacer las nuevas dependencias:

`sudo apt-get dist-upgrade`
