# apt

> Herramienta de gestión de paquete para distribuciones basadas en Debian.
> Se recomienda sustituirlo por apt-get cuando se use interactivamente en Ubuntu 16.04 o versiones posteriores.

- Actualiza la lista de paquetes y versiones disponibles (se recomienda ejecutar este comando antes que cualquier otro comando `apt`):

`sudo apt update`

- Busca un paquete:

`apt search {{paquete}}`

- Mostrar información para un paquete:

`apt show {{paquete}}`

- Instalar un paquete o actualizarlo a su última versión disponible:

`sudo apt install {{paquete}}`

- Eliminar un paquete (si se utiliza `purge` también se elimina sus archivos de configuración):

`sudo apt remove {{paquete}}`

- Actualizar todos los paquetes a sus nuevas versiones disponibles:

`sudo apt upgrade`

- Mostrar todos los paquetes:

`apt list`

- Mostrar los paquetes instalados:

`apt list --installed`
