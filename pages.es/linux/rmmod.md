# rmmod

> Elimina módulos del núcleo Linux.
> Vea también: `kmod`, para otros comandos de gestión de módulos.
> Más información: <https://manned.org/rmmod>.

- Elimina un módulo del kernel:

`sudo rmmod {{nombre_del_módulo}}`

- Elimina un módulo del kernel y muestra información detallada:

`sudo rmmod --verbose {{nombre_del_módulo}}`

- Elimina un módulo del kernel y envía los errores a syslog en lugar de a `stderr`:

`sudo rmmod --syslog {{nombre_del_modulo}}`

- Muestra la ayuda:

`rmmod --help`

- Muestra la versión:

`rmmod --version`
