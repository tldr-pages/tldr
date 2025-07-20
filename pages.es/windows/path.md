# path

> Mostrar o establecer la ruta de búsqueda para archivos ejecutables.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/path>.

- Mostrar la ruta actual:

`path`

- Establecer la ruta a uno o más directorios separados por punto y coma:

`path {{ruta\al\directorio1 ruta\al\directorio2 ...}}`

- Agregar un nuevo directorio a la ruta original:

`path {{ruta\al\directorio}};%path%`

- Establecer el símbolo del sistema para que solo busque en el directorio actual archivos ejecutables:

`path ;`
