# systemctl disable

> Desactiva servicios de systemd.
> Más información: <https://www.freedesktop.org/software/systemd/man/systemctl.html#disable%20UNIT%E2%80%A6>.

- Evita que un servicio se ejecute al arrancar:

`systemctl disable {{unidad}}`

- Evita que un servicio se ejecute al arrancar y detiene su ejecución actual:

`systemctl disable {{unidad}} --now`

- Evita que un servicio de usuario se ejecute al iniciar sesión:

`systemctl disable {{unidad}} --user`
