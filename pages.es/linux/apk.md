# apk

> Herramienta de gestión de paquetes de Alpine Linux.
> Más información: <https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management>.

- Actualizar los índices de repositorio desde todos los repositorios remotos:

`apk update`

- Instalar un nuevo paquete:

`apk add {{paquete}}`

- Eliminar un paquete:

`apk del {{paquete}}`

- Reparar paquete o actualizarlo sin modificar dependencias principales:

`apk fix {{paquete}}`

- Buscar paquete mediante palabra clave:

`apk search {{palabra clave}}`

- Obtener información sobre un paquete en específico:

`apk info {{paquete}}`
