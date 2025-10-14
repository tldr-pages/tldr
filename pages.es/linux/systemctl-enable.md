# systemctl enable

> Activa servicios de systemd.
> Más información: <https://www.freedesktop.org/software/systemd/man/systemctl.html#enable%20UNIT%E2%80%A6>.

- Activa un servicio para que se ejecute al arrancar:

`systemctl enable {{unidad}}`

- Activa un servicio para que se ejecute al arrancar y lo inicia ahora:

`systemctl enable {{unidad}} --now`

- Activa una unidad de usuario para que se ejecute al iniciar sesión:

`systemctl enable {{unidad}} --user`
