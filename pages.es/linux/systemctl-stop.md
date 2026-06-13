# systemctl stop

> Detiene unidades systemd.
> Más información: <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#stop%20PATTERN%E2%80%A6>.

- Detiene una unidad:

`systemctl stop {{unidad}}`

- Detiene un servicio y suprimir las advertencias:

`systemctl stop {{unidad}} --no-warn`

- Detiene una unidad de usuario:

`systemctl stop {{unidad}} --user`
