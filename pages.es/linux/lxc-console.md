# lxc-console

> Se conecta a un contenedor.
> Más información: <https://linuxcontainers.org/lxc/manpages//man1/lxc-console.1.html>.

- Inicia una consola en un contenedor:

`agetty {{[-L|--local-line]}} {{38400}} tty1`

- Se conecta a una consola lxc:

`sudo lxc-console {{nombre_del_contenedor}}`

- Sale de `lxc-console`:

`<Ctrl a><q>`

- Muestra la ayuda:

`lxc-console {{[-?|--help]}}`
