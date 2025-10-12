# chroot

> Ejecuta un comando o un intérprete de comandos interactivo con un directorio raíz especial.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>.

- Ejecuta un comando como nuevo directorio raíz:

`sudo chroot {{ruta/al/nuevo/root}} {{comando}}`

- Utiliza un usuario y grupo específicos:

`sudo chroot --userspec {{nombre_usuario_o_id:nombre_grupo_o_id}}`
