# bpkg

> Un gestor de paquetes para scripts Bash.
> Más información: <https://github.com/bpkg/bpkg>.

- Actualiza el índice local:

`bpkg update`

- Instala un paquete globalmente:

`bpkg install --global {{paquete}}`

- Instala un paquete en un subdirectorio del directorio actual:

`bpkg install {{paquete}}`

- Instala una versión específica de un paquete de forma global:

`bpkg install {{paquete}}@{{versión}} -g`

- Muestra detalles sobre un paquete específico:

`bpkg show {{paquete}}`

- Ejecuta un comando, especificando opcionalmente sus argumentos:

`bpkg run {{comando}} {{argumento1 argumento2 ...}}`
