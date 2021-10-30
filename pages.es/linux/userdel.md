# userdel

> Elimina una cuenta de usuario o elimina un usuario de un grupo.
> Nota: todos los comandos deben ser ejecutados como root.
> Más información: <https://manned.org/userdel>.

- Elimina un usuario:

`userdel {{nombre}}`

- Elimina un usuario junto con su directorio home y mail spool:

`userdel --remove {{nombre}}`

- Elimina un usuario de un grupo:

`userdel {{nombre}} {{grupo}}`

- Elimina un usuario en otro directorio root:

`userdel --root {{ruta/al/otro/root}} {{nombre}}`
