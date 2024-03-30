# aptitude

> Herramienta de gestión de paquetes para Debian y Ubuntu.
> Más información: <https://manpages.debian.org/latest/aptitude/aptitude.8.html>.

- Sincroniza la lista de paquetes y versiones disponible (se recomienda ejecutar este comando antes que cualquier otro comando `aptitude`):

`aptitude update`

- Instala un nuevo paquete y sus dependencias:

`aptitude install {{paquete}}`

- Busca un paquete:

`aptitude search {{paquete}}`

- Busca un paquete instalado (`?installed` es un término de búsqueda de `aptitude`):

`aptitude search '?installed({{paquete}})'`

- Elimina un paquete y todos los paquetes que dependen de él:

`aptitude remove {{paquete}}`

- Actualiza todos los paquetes a sus nuevas versiones disponibles:

`aptitude upgrade`

- Actualiza paquetes instalados (como `aptitude upgrade`), elimina los paquetes obsoletos e instala paquetes adicionales para satisfacer sus dependencias:

`aptitude full-upgrade`

- Mantiene un paquete instalado para que no sea actualizado automáticamente:

`aptitude hold '?installed({{paquete}})'`
