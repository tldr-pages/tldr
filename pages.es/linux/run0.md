# run0

> Eleva privilegios interactivamente.
> Similar a `sudo`, pero no es un binario SUID, la autenticación tiene lugar a través de polkit, y los comandos se invocan desde un servicio `systemd`.
> Más información: <https://www.freedesktop.org/software/systemd/man/run0.html>.

- Ejecuta un comando como root:

`run0 {{comando}}`

- Ejecuta un comando como otro usuario y/o grupo:

`run0 {{[-u|--user]}} {{usuario|uid}} {{[-g|--group]}} {{nombre_de_grupo|gid}} {{comando}}`
