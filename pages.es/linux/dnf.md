# dnf

> Gestor de paquetes para Fedora 41+ y RHEL 10.
> Vea los comandos equivalentes en otros gestores de paquetes en <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Más información: <https://dnf5.readthedocs.io/en/latest/commands/index.html>.

- Actualiza los paquetes instalados a las últimas versiones disponibles:

`sudo dnf {{[up|upgrade]}}`

- Busca paquetes por palabras clave:

`dnf {{[se|search]}} {{keyword1 keyword2 ...}}`

- Muestra detalles sobre un paquete:

`dnf {{[if|info]}} {{paquete}}`

- Instala nuevos paquetes (utilice `--assumeyes` para confirmar automáticamente todas las solicitudes):

`sudo dnf {{[in|install]}} {{paquete1 paquete2 ...}}`

- Elimina paquetes:

`sudo dnf {{[rm|remove]}} {{paquete1 paquete2 ...}}`

- Muestra una lista de los paquetes instalados:

`dnf {{[ls|list]}} --installed`

- Busca qué paquetes proporcionan un comando determinado:

`dnf provides {{comando}}`

- Limpia los datos almacenados en caché:

`sudo dnf clean {{all|dbcache|expire-cache|metadata|packages}}`
