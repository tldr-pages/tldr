# usermod

> Modifica una cuenta de usuario.
> Vea también: `users`, `useradd`, `userdel`.
> Más información: <https://manned.org/usermod>.

- Cambia el nombre de un usuario:

`sudo usermod {{[-l|--login]}} {{nuevo_nombre}} {{usuario}}`

- Cambia el ID de un usuario:

`sudo usermod {{[-u|--uid]}} {{id}} {{usuario}}`

- Cambia la interfaz de comandos (shell) a un usuario:

`sudo usermod {{[-s|--shell]}} {{ruta/a/interfaz_comando}} {{usuario}}`

- Añade un usuario a grupos suplementarios (ten en cuenta los espacios en blanco):

`sudo usermod {{[-a|--append]}} {{[-G|--groups]}} {{grupo1,grupo2}} {{usuario}}`

- Cambia el directorio home de un usuario:

`sudo usermod {{[-m|--move-home]}} {{[-d|--home]}} {{ruta/al/nuevo_home}} {{usuario}}`
