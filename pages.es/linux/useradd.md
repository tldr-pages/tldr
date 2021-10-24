# useradd

> Crea un usuario nuevo.
> Más información: <https://manned.org/useradd>.

- Crea un usuario nuevo:

`useradd {{nombre}}`

- Crea un usuario nuevo con el directorio home predeterminado:

`useradd --create-home {{nombre}}`

- Crea un usuario nuevo con una shell específica:

`useradd --shell {{ruta/a/la/shell}} {{nombre}}`

- Crea un usuario nuevo perteneciente a grupos adicionales (tener en cuenta que no existen espacios en blanco):

`useradd --groups {{grupo1,grupo2}} {{nombre}}`

- Crea un usuario nuevo del sistema sin directorio home:

`useradd --no-create-home --system {{nombre}}`
