# dpkg-query

> Muestra información sobre paquetes instalados.
> Más información: <https://manned.org/dpkg-query.1>.

- Lista todos los paquetes instalados:

`dpkg-query --list`

- Lista de paquetes instalados que coinciden con un patrón:

`dpkg-query --list '{{libc6*}}'`

- Lista todos los archivos instalados por un paquete:

`dpkg-query --listfiles {{libc6}}`

- Muestra información sobre un paquete:

`dpkg-query --status {{libc6}}`

- Busca paquetes que tengan archivos que coincidan con un patrón:

`dpkg-query --search {{/etc/ld.so.conf.d}}`
