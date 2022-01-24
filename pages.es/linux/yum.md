# yum

> Administrador de paquetes para RHEL, CentOS y Fedora (para versiones anteriores).
> Más información: <https://manned.org/yum>.

- Instala un nuevo paquete:

`yum install {{package}}`

- Instala un nuevo paquete respondiendo si a todas las preguntas (también trabaja con actualizaciones, util para actualizaciones automáticas):

`yum -y install {{package}}`

- Encuentra que paquete provee un archivo determinado:

`yum provides {{command}}`

- Elimina un paquete:

`yum remove {{package}}`

- Muestra las actualizaciones disponibles para los paquetes instalados:

`yum check-update`

- Actualiza los paquetes instalados a las versiones más recientes disponibles:

`yum upgrade`
