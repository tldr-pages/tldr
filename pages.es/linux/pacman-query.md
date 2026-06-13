# pacman --query

> Consulta la base de datos local de paquetes.
> Vea también: `pacman`.
> Más información: <https://manned.org/pacman.8>.

- [C]onsulta la base de datos local de paquetes y muestra los paquetes instalados y sus versiones:

`pacman -Q`

- Muestra solo los paquetes y versiones que se instalaron [e]xplicitamente:

`pacman -Qe`

- Averigua qué paquete gestiona un archivo:

`pacman -Qo {{nombre_archivo}}`

- Muestra información sobre un paquete [i]nstalado:

`pacman -Qi {{paquete}}`

- Muestra la [l]ista de archivos que pertenecen a un paquete específico:

`pacman -Ql {{paquete}}`

- Muestra los paquetes huérfanos (instalados como [d]ependencias pero que ningún paquete ([t]) requiere, y los muestra en modo [q]uieto (solo se muestra el nombre del paquete)):

`pacman -Qdtq`

- Muestra los paquetes instalados ajenos ([m]) a la base de datos del repositorio:

`pacman -Qm`

- Muestra los paquetes que se pueden [a]ctualizar:

`pacman -Qu`
