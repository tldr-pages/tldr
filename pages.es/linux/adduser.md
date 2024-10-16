# adduser

> Utilidad de adición de usuarios.
> Más información: <https://manned.org/adduser>.

- Crea un nuevo usuario con un directorio home predeterminado y solicita al usuario que establezca una contraseña:

`adduser {{nombre_de_usuario}}`

- Crea un nuevo usuario sin un directorio home:

`adduser --no-create-home {{nombre_de_usuario}}`

- Crea un nuevo usuario con un directorio home en la ruta especificada:

`adduser --home {{ruta/a/home}} {{nombre_de_usuario}}`

- Crea un nuevo usuario con el intérprete de comandos especificado establecido como intérprete de comandos de inicio de sesión:

`adduser --shell {{ruta/a/shell}} {{nombre_de_usuario}}`

- Crea un nuevo usuario que pertenezca al grupo especificado:

`adduser --ingroup {{group}} {{nombre_de_usuario}}`
