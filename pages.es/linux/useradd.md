# useradd

> Crea un usuario.
> Vea también: `users`, `userdel`, `usermod`.
> Más información: <https://manned.org/useradd>.

- Crea un usuario:

`sudo useradd {{usuario}}`

- Crea un usuario con el ID de usuario específico:

`sudo useradd {{[-u|--uid]}} {{id}} {{usuario}}`

- Crea un usuario con una línea de comando (shell) específica:

`sudo useradd {{[-s|--shell]}} {{ruta/a/la/shell}} {{usuario}}`

- Crea un usuario perteneciente a grupos adicionales (ten en cuenta que no se colocan espacios en blanco):

`sudo useradd {{[-G|--groups]}} {{grupo1,grupo2,...}} {{usuario}}`

- Crea un usuario con el directorio home predeterminado:

`sudo useradd {{[-m|--create-home]}} {{usuario}}`

- Crea un usuario con el directorio home con una copia de los archivos provenientes de un directorio plantilla:

`sudo useradd {{[-k|--skel]}} {{ruta/a/directorio_plantilla}} {{[-m|--create-home]}} {{usuario}}`

- Crea un usuario del sistema sin directorio home:

`sudo useradd {{[-r|--system]}} {{usuario}}`
