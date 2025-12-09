# lxc-create

> Crea contenedores linux.
> Más información: <https://linuxcontainers.org/lxc/getting-started/>.

- Crea un contenedor interactivamente en `/var/lib/lxc/`:

`sudo lxc-create {{[-n|--name]}} {{contenedor}} {{[-t|--template]}} download`

- Crea un contenedor en un directorio de destino:

`sudo lxc-create {{[-P|--lxcpath]}} {{/ruta/al/directorio/}} {{[-n|--name]}} {{contenedor}} {{[-t|--template]}} download`

- Crea un contenedor pasando opciones a una plantilla:

`sudo lxc-create {{[-n|--name]}} {{nombre}} {{[-t|--template]}} download -- {{[-d|--dist]}} {{nombre-distro}} {{[-r|--release]}} {{versión-de-lanzamiento}} {{[-a|--arch]}} {{arch}}`

- Muestra ayuda:

`lxc-create {{[-?|--help]}}`
