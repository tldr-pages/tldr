# usermod

> Modifica una cuenta de usuario.
> Vea también: `users`, `useradd`, `userdel`.
> Más información: <https://manned.org/usermod>.

- Cambia el nombre de un usuario:

`sudo usermod -l {{nuevo_nombre}} {{usuario}}`

- Cambia el ID de un usuario:

`sudo usermod --uid {{id}} {{nombre_usuario}}`

- Cambia la interfaz de comandos (shell) a un usuario:

`sudo usermod --shell {{ruta/a/interfaz_comando}} {{nombre_usuario}}`

- Añade un usuario a grupos suplementarios (ten en cuenta los espacios en blanco):

`sudo usermod -a -G {{grupo1,grupo2}} {{usuario}}`

- Cambia el directorio home de un usuario:

`usermod -m -d {{ruta/al/nuevo_home}} {{usuario}}`
