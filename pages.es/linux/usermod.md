# usermod

> Modifica una cuenta de usuario.
> Más información: <https://manned.org/usermod>.

- Cambia el nombre de un usuario:

`usermod -l {{nuevo_nombre}} {{usuario}}`

- Añade un usuario a grupos suplementarios (tener en cuenta los espacios en blanco):

`usermod -a -G {{grupo1,grupo2}} {{usuario}}`

- Crea un nuevo directorio home para un usuario y mueve sus archivos a él:

`usermod -m -d {{ruta/al/home}} {{usuario}}`
