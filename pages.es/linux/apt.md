# apt

> Herramienta de gestión de paquete para distribuciones basadas en Debian.
> Se recomienda sustituirlo por `apt-get` cuando se use interactivamente en Ubuntu 16.04 o versiones posteriores.
> Más información: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Actualiza la lista de paquetes y versiones disponibles (se recomienda ejecutar este comando antes que cualquier otro comando `apt`):

`sudo apt update`

- Busca un paquete:

`apt search {{paquete}}`

- Muestra la información de un paquete:

`apt show {{paquete}}`

- Instala un paquete o lo actualiza a su última versión disponible:

`sudo apt install {{paquete}}`

- Elimina un paquete (si se utiliza `purge` también elimina sus archivos de configuración):

`sudo apt remove {{paquete}}`

- Actualiza todos los paquetes a sus nuevas versiones disponibles:

`sudo apt upgrade`

- Muestra todos los paquetes:

`apt list`

- Muestra los paquetes instalados:

`apt list --installed`
