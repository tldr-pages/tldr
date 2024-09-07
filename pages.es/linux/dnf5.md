# dnf5

> Programa de gestión de paquetes para RHEL, Fedora y CentOS (reemplaza a dnf, que a su vez reemplazó a yum).
> DNF5 es una reescritura en C++ del gestor de paquetes DNF con mejor rendimiento y menor tamaño.
> Para comandos equivalentes en otros gestores de paquetes, vea <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Más información: <https://dnf5.readthedocs.io/>.

- Actualiza los paquetes instalados a las versiones más recientes disponibles:

`sudo dnf5 upgrade`

- Busca paquetes mediante palabras clave:

`dnf5 search {{palabra_clave1 palabra_clave2 ...}}`

- Muestra detalles sobre un paquete:

`dnf5 info {{paquete}}`

- Instala nuevos paquetes (Nota: usa la opción `-y` para saltar todas las confirmaciones):

`sudo dnf5 install {{paquete1 paquete2 ...}}`

- Elimina paquetes:

`sudo dnf5 remove {{paquete1 paquete2 ...}}`

- Lista paquetes instalados:

`dnf5 list --installed`

- Busca que paquetes proporcionan un comando determinado:

`dnf5 provides {{comando}}`

- Elimina o expira los datos almacenados en caché:

`sudo dnf5 clean all`
