# dpkg-query

> Muestra información sobre paquetes instalados.
> Más información: <https://manned.org/dpkg-query>.

- Lista todos los paquetes instalados:

`dpkg-query {{[-l|--list]}}`

- Lista de paquetes instalados que coinciden con un patrón:

`dpkg-query {{[-l|--list]}} '{{libc6*}}'`

- Lista todos los archivos instalados por un paquete:

`dpkg-query {{[-L|--listfiles]}} {{libc6}}`

- Muestra información sobre un paquete:

`dpkg-query {{[-s|--status]}} {{libc6}}`

- Busca paquetes que tengan archivos que coincidan con un patrón:

`dpkg-query {{[-S|--search]}} {{/etc/ld.so.conf.d}}`
