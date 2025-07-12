# cmdkey

> Crea, muestra y elimina nombres de usuario y contraseñas almacenados.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmdkey>.

- Listar todas las credenciales de usuario:

`cmdkey /list`

- Almacenar credenciales para un usuario que accede a un servidor:

`cmdkey /add:{{nombre_del_servidor}} /user:{{nombre_de_usuario}}`

- Eliminar credenciales para un objetivo específico:

`cmdkey /delete {{nombre_del_objetivo}}`
