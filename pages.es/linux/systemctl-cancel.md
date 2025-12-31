# systemctl cancel

> Cancela uno o más trabajos pendientes en el administrador del sistema o de usuario.
> Más información: <https://www.freedesktop.org/software/systemd/man/systemctl.html#cancel%20JOB%E2%80%A6>.

- Cancela un trabajo por su ID numérico:

`systemctl cancel {{id_trabajo}}`

- Cancela múltiples trabajos:

`systemctl cancel {{id_trabajo1 id_trabajo2 ...}}`

- Cancela todos los trabajos pendientes:

`systemctl cancel`

- Cancela un trabajo en el administrador de servicios de usuario:

`systemctl cancel {{id_trabajo}} --user`
