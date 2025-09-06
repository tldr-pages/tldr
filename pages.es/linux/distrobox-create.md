# distrobox-create

> Crea un contenedor Distrobox. Véase también: `tldr distrobox`.
> El contenedor creado se integrará estrechamente con el anfitrión, permitiendo compartir el directorio HOME del usuario, almacenamiento externo, dispositivos USB externos, aplicaciones gráficas (X11/Wayland) y audio.
> Más información: <https://distrobox.it/usage/distrobox-create>.

- Crea un contenedor Distrobox utilizando la imagen Ubuntu:

`distrobox-create {{nombre_del_contenedor}} --image {{ubuntu:latest}}`

- Clona un contenedor Distrobox:

`distrobox-create --clone {{nombre_del_contenedor}} {{nombre_del_contenedor_clonado}}`
