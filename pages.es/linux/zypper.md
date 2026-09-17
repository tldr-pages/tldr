# zypper

> Utilidad para la gestión de paquetes en SUSE y openSUSE.
> Más información: <https://en.opensuse.org/SDB:Zypper_manual>.

- Sincroniza la lista de paquetes y versiones disponibles:

`sudo zypper {{[ref|refresh]}}`

- Instala un nuevo paquete:

`sudo zypper {{[in|install]}} {{paquete}}`

- Elimina un paquete:

`sudo zypper {{[rm|remove]}} {{paquete}}`

- Actualiza los paquetes instalados a la versión más reciente disponible:

`sudo zypper {{[up|update]}}`

- Busca en los repositorios un paquete mediante una palabra clave:

`zypper {{[se|search]}} {{palabra_clave}}`

- Muestra información relacionada con los repositorios configurados:

`zypper {{[lr|repos]}} --sort-by-priority`
