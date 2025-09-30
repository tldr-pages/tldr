# dnf group

> Gestiona colecciones virtuales de paquetes en sistemas basados en Fedora.
> Más información: <https://dnf.readthedocs.io/en/latest/command_ref.html#group-command>.

- Lista grupos DNF, mostrando el estado de instalado y desinstalado en una tabla:

`dnf {{[grp|group]}} list`

- Muestra información del grupo DNF, incluyendo repositorio y paquetes opcionales:

`dnf {{[grp|group]}} info {{nombre_grupo}}`

- Instala un grupo DNF:

`dnf {{[grp|group]}} install {{nombre_grupo}}`

- Elimina un grupo DNF:

`dnf {{[grp|group]}} remove {{nombre_grupo}}`

- Actualiza un grupo DNF:

`dnf {{[grp|group]}} upgrade {{nombre_grupo}}`
