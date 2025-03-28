# dnf group

> Gestiona colecciones virtuales de paquetes en sistemas basados en Fedora.
> Más información: <https://manned.org/dnf-group>.

- Lista los grupos DNF, mostrando el estado de instalado o no en una tabla:

`dnf group list`

- Muestra información del grupo DNF, incluyendo repositorio y paquetes opcionales:

`dnf group info {{nombre_del_grupo}}`

- Instala un grupo DNF:

`dnf group install {{nombre_del_grupo}}`

- Elimina un grupo DNF:

`dnf group remove {{nombre_del_grupo}}`

- Actualiza un grupo DNF:

`dnf group upgrade {{nombre_del_grupo}}`
