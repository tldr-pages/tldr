# yum

> Administrador de paquetes para RHEL, CentOS y Fedora (para versiones anteriores).
> Más información: <https://man7.org/linux/man-pages/man8/yum.8.html>.

- Instala un nuevo paquete:

`yum install {{package}}`

- Instala un nuevo paquete respondiendo si a todas las preguntas:

`yum -y install {{package}}`

- Encuentra que paquete provee un archivo determinado:

`yum provides {{command}}`

- Elimina un paquete

`yum remove {{package}}`

- Muestra las actualizaciones disponibles para los paquetes instalados:

`yum check-update`

- Actualice los paquetes instalados a las versiones más recientes disponibles:

`yum upgrade`
