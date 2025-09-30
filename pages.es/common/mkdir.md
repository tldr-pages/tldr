# mkdir

> Crea directorios y establece sus permisos.
> Vea también: `rmdir`, `ls`.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html>.

- Crea los directorios especificados:

`mkdir {{ruta/al/directorio1 ruta/al/directorio2 ...}}`

- Crea directorios recursivamente y sus padres si es necesario:

`mkdir {{[-p|--parents]}} {{ruta/al/directorio}}`

- Crea directorios con permisos específicos:

`mkdir {{[-m|--mode]}} {{rwxrw-r--}} {{ruta/al/directorio1 ruta/al/directorio2 ...}}`
