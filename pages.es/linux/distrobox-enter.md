# distrobox-enter

> Entra a un contenedor Distrobox. Véase también: `tldr distrobox`.
> El comando ejecutado por defecto es su SHELL, pero puede especificar otros o comandos enteros a ejecutar. Si se utiliza dentro de un script, una aplicación o un servicio, puede utilizar el modo `--headless` para desactivar tty e interactividad.
> Más información: <https://distrobox.it/usage/distrobox-enter>.

- Entra a un contenedor Distrobox:

`distrobox-enter {{nombre_del_contenedor}}`

- Entra a un contenedor Distrobox y ejecuta un comando al iniciar sesión:

`distrobox-enter {{nombre_del_contenedor}} -- {{sh -l}}`

- Entra a un contenedor Distrobox sin instanciar una tty:

`distrobox-enter --name {{nombre_del_contenedor}} -- {{uptime -p}}`
