# autojump

> Salta rápidamente entre los directorios que más visitas.
> Se proporcionan alias como `j` o `jc` para escribir aún menos.
> Vea también: «bashmarks».
> Más información: <https://github.com/wting/autojump>.

- Añade los alias `autojump` a tu intérprete de comandos:

`source /usr/share/autojump/autojump.{{bash|fish|zsh}}`

- Salta a un directorio que contenga el patrón dado:

`j {{patrón}}`

- Salta a un subdirectorio (hijo) del directorio actual que contenga el patrón dado:

`jc {{patrón}}`

- Abre un directorio que contenga el patrón dado en el gestor de archivos del sistema operativo:

`jo {{patrón}}`

- Elimina directorios que no existen de la base de datos `autojump`:

`j --purge`

- Mustra las entradas de la base de datos `autojump`:

`j {{[-s|--stat]}}`
