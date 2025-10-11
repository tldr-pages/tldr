# systemctl exit

> Solicita al administrador de servicios que salga.
> Más información: <https://www.freedesktop.org/software/systemd/man/systemctl.html#exit%20EXIT_CODE>.

- Sale del administrador de servicios de usuario:

`systemctl exit --user`

- Sale del administrador de servicios de usuario con un código de salida específico:

`systemctl exit {{codigo}} --user`

- Solicita al administrador de servicios del contenedor que salga (equivalente a `systemctl poweroff` si no está en un contenedor):

`systemctl exit`
