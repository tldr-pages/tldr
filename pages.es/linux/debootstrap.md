# debootstrap

> Crea un sistema básico de Debian.
> Más información: <https://wiki.debian.org/Debootstrap>.

- Crea un sistema de la versión estable de Debian dentro del directorio `debian-root`:

`sudo debootstrap stable {{ruta/a/debian-root/}} http://deb.debian.org/debian`

- Crea un sistema mínimo que incluye solo los paquetes necesarios:

`sudo debootstrap --variant=minbase stable {{ruta/a/debian-root/}}`

- Crea un sistema Ubuntu 20.04 dentro del directorio `focal-root` con un espejo local:

`sudo debootstrap focal {{ruta/a/focal-root/}} {{file:///ruta/a/mirror/}}`

- Cambia a un sistema de arranque:

`sudo chroot {{ruta/a/root}}`

- Lista las versiones mayores disponibles:

`ls /usr/share/debootstrap/scripts/`
