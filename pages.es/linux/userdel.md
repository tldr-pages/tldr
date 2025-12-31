# userdel

> Elimina una cuenta de usuario o elimina un usuario de un grupo.
> Vea también: `users`, `useradd`, `usermod`.
> Más información: <https://manned.org/userdel>.

- Elimina un usuario:

`sudo userdel {{usuario}}`

- Elimina un usuario en otro directorio raíz:

`sudo userdel {{[-R|--root]}} {{ruta/al/otro/root}} {{usuario}}`

- Elimina un usuario junto con su directorio home y correo (mail spool):

`sudo userdel {{[-r|--remove]}} {{usuario}}`
