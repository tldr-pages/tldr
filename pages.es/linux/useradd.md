# useradd

> Crea un usuario nuevo.
> Ver también: `users`, `userdel`, `usermod`.
> Más información: <https://manned.org/useradd>.

- Crea un usuario nuevo:

`sudo useradd {{usuario}}`

- Crea un usuario nuevo con el ID de usuario específico:

`sudo useradd --uid {{id}} {{usuario}}`

- Crea un usuario nuevo con una línea de comando(shell) específica:

`sudo useradd --shell {{ruta/a/la/shell}} {{usuario}}`

- Crea un usuario nuevo perteneciente a grupos adicionales (tener en cuenta que no se colocan espacios en blanco):

`sudo useradd --groups {{grupo1,grupo2}} {{usuario}}`

- Crea un usuario nuevo con el directorio home predeterminado:

`sudo useradd --create-home {{usuario}}`

- Crea un usuario nuevo con el directorio home con copia de los archivos definidos en un directorio plantilla:

`sudo useradd --skel {{ruta/a/directorio_plantilla}} --create-home {{usuario}}`

- Crea un usuario nuevo del sistema sin directorio home:

`sudo useradd --no-create-home --system {{usuario}}`
