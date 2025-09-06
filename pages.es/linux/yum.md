# yum

> Administrador de paquetes para RHEL, CentOS y Fedora (para versiones anteriores).
> Más información: <https://manned.org/yum>.

- Instala un nuevo paquete:

`yum install {{paquete}}`

- Instala un nuevo paquete respondiendo sí a todas las preguntas (también trabaja con actualizaciones, útil para actualizaciones automáticas):

`yum -y install {{paquete}}`

- Encuentra que paquete provee un archivo determinado:

`yum provides {{comando}}`

- Elimina un paquete:

`yum remove {{paquete}}`

- Muestra las actualizaciones disponibles para los paquetes instalados:

`yum check-update`

- Actualiza los paquetes instalados a las versiones más recientes disponibles:

`yum upgrade`
