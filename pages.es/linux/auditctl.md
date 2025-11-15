# auditctl

> Utilidad para controlar el comportamiento, obtener el estado y gestionar las reglas del Sistema de Auditoría de Linux.
> Más información: <https://manned.org/auditctl>.

- Muestra el e[s]tado del sistema de auditoría:

`sudo auditctl -s`

- Muestra todas las reglas de auditoría cargadas actualmente:

`sudo auditctl -l`

- Elimina todas las reglas de auditoría:

`sudo auditctl -D`

- Habilita/deshabilita el sistema de auditoría:

`sudo auditctl -e {{1|0}}`

- Vigila un archivo en busca de cambios:

`sudo auditctl -a always,exit -F arch=b64 -F path={{/ruta/al/archivo}} -F perm=wa`

- Busca cambios en un directorio de forma recursiva:

`sudo auditctl -a always,exit -F arch=b64 -F dir={{/ruta/al/directorio/}} -F perm=wa`

- Muestra ayuda:

`auditctl -h`
