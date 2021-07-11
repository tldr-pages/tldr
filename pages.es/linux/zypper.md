# zypper

> Utilidad para la gestión de paquetes en SUSE y openSUSE.
> Más información: <https://en.opensuse.org/SDB:Zypper_manual>

- Actualiza todos los repositorios:

`zypper refresh`

- Instala un nuevo paquete:

`zypper install {{paquete}}`

- Elimina un paquete:

`zypper remove {{paquete}}`

- Actualiza los paquetes instalados a la última versión disponible:

`zypper update`

- Busca en los repositorios un paquete mediante una palabra clave:

`zypper search {{palabra_clave}}`

- Muestra un listado con la información de los repositorios configurados:

`zypper repos -P`
