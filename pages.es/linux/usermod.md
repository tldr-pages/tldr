# usermod

> Modifica una cuenta de usuario.
> Ver también: `users`, `useradd`, `userdel`.
> Más información: <https://manned.org/usermod>.

- Cambia el nombre de un usuario:

`usermod -l {{nuevo_nombre}} {{usuario}}`

- Cambia el ID de un usuario:

`sudo usermod --uid {{id}} {{nombre_usuario}}`

- Cambia la interfaz de comandos(shell) a un usuario:

`sudo usermod --shell {{path/to/shell}} {{username}}`

- Añade un usuario a grupos suplementarios (tener en cuenta los espacios en blanco):

`usermod -a -G {{grupo1,grupo2}} {{usuario}}`

- Crea un nuevo directorio home para un usuario y mueve sus archivos a él:

`usermod -m -d {{ruta/al/home}} {{usuario}}`
