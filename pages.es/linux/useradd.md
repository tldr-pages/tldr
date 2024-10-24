# useradd

> Crea un usuario.
> Ver también: `users`, `userdel`, `usermod`.
> Más información: <https://manned.org/useradd>.

- Crea un usuario:

`sudo useradd {{usuario}}`

- Crea un usuario con el ID de usuario específico:

`sudo useradd --uid {{id}} {{usuario}}`

- Crea un usuario con una línea de comando(shell) específica:

`sudo useradd --shell {{ruta/a/la/shell}} {{usuario}}`

- Crea un usuario perteneciente a grupos adicionales (tener en cuenta que no se colocan espacios en blanco):

`sudo useradd --groups {{grupo1,grupo2}} {{usuario}}`

- Crea un usuario con el directorio home predeterminado:

`sudo useradd --create-home {{usuario}}`

- Crea un usuario con el directorio home con una copia de los archivos provenientes de un directorio plantilla:

`sudo useradd --skel {{ruta/a/directorio_plantilla}} --create-home {{usuario}}`

- Crea un usuario del sistema sin directorio home:

`sudo useradd --system {{usuario}}`
