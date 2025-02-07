# lxc-create

> Crea contenedores linux.
> Más información: <https://linuxcontainers.org/lxc/getting-started>.

- Crea un contenedor interactivamente en `/var/lib/lxc/`:

`lxc-create --name {{contenedor}} --template download`

- Crea un contenedor en un directorio de destino:

`lxc-create --lxcpath {{/ruta/a/directorio/}} --name {{contenedor}} --template download`

- Crea un contenedor pasando opciones a una plantilla:

`lxc-create --name {{nombre}} --template download -- --dist {{nombre-distro}} --release {{versión-de-lanzamiento}} --arch {{arch}}`
