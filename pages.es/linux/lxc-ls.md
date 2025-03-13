# lxc-ls

> Lista contenedores Linux.
> Más información: <https://linuxcontainers.org/lxc/manpages/man1/lxc-ls.1.html>.

- Lista contenedores activos (incluyendo congelados y en ejecución):

`lxc-ls --active`

- Lista solo contenedores congelados:

`lxc-ls --frozen`

- Lista solo contenedores parados:

`lxc-ls --stopped`

- Lista contenedores en una salida elegante, basada en columnas:

`sudo lxc-ls {{[-f|--fancy]}}`
