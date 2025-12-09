# zypper

> Utilidad para la gestión de paquetes en SUSE y openSUSE.
> Más información: <https://en.opensuse.org/SDB:Zypper_manual>.

- Sincroniza la lista de paquetes y versiones disponibles:

`zypper refresh`

- Instala un nuevo paquete:

`zypper install {{paquete}}`

- Elimina un paquete:

`zypper remove {{paquete}}`

- Actualiza los paquetes instalados a la versión más reciente disponible:

`zypper update`

- Busca en los repositorios un paquete mediante una palabra clave:

`zypper search {{palabra_clave}}`

- Muestra información relacionada con los repositorios configurados:

`zypper repos --sort-by-priority`
