# apk

> Herramienta de gestión de paquetes de Alpine Linux.
> Más información: <https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>.

- Actualiza los índices de repositorio desde todos los repositorios remotos:

`apk update`

- Instala un nuevo paquete:

`apk add {{paquete}}`

- Remueve un paquete:

`apk del {{paquete}}`

- Repara un paquete o lo actualiza sin modificar dependencias principales:

`apk fix {{paquete}}`

- Busca un paquete usando palabras clave:

`apk search {{palabras_clave}}`

- Muestra información sobre un paquete específico:

`apk info {{paquete}}`
